import os
import fitz
import pickle

from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


PDF_FOLDER = "documents"
INDEX_FILE = "companies_act_index_nomic-embed-text-v2-moe_chunk2000_overlap300.pkl"


# ------------------------------------------------------------
# 1. Split long text into smaller chunks
# ------------------------------------------------------------
def chunk_text(text, chunk_size=2000, overlap=300):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end]

        if chunk.strip():
            chunks.append(chunk)

        start += chunk_size - overlap

    return chunks


# ------------------------------------------------------------
# 2. Read text from PDF files
# ------------------------------------------------------------
def load_pdf_text(folder):
    all_text = ""

    for filename in os.listdir(folder):
        if filename.lower().endswith(".pdf"):
            file_path = os.path.join(folder, filename)
            print(f"Reading: {filename}")

            doc = fitz.open(file_path)

            for page in doc:
                all_text += page.get_text()

            doc.close()

    return all_text


# ------------------------------------------------------------
# 3. Build or load saved RAG index
# ------------------------------------------------------------
def build_simple_index():
    if os.path.exists(INDEX_FILE):
        print("Loading saved RAG index...")

        with open(INDEX_FILE, "rb") as file:
            saved_data = pickle.load(file)

        chunks = saved_data["chunks"]
        chunk_vectors = saved_data["chunk_vectors"]

        embeddings = OllamaEmbeddings(model="nomic-embed-text-v2-moe")

        print("Saved RAG index loaded.")

        return chunks, chunk_vectors, embeddings

    print("No saved index found. Building new RAG index...")

    print("Loading PDF...")
    text = load_pdf_text(PDF_FOLDER)

    print("Chunking text...")
    chunks = chunk_text(text)

    print(f"Total chunks created: {len(chunks)}")

    print("Creating embeddings...")
    embeddings = OllamaEmbeddings(model="nomic-embed-text-v2-moe")

    chunk_vectors = []
    batch_size = 20

    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        print(f"Embedding chunks {i + 1} to {i + len(batch)} of {len(chunks)}")

        batch_vectors = embeddings.embed_documents(batch)
        chunk_vectors.extend(batch_vectors)

    print("Saving RAG index...")

    saved_data = {
        "chunks": chunks,
        "chunk_vectors": chunk_vectors
    }

    with open(INDEX_FILE, "wb") as file:
        pickle.dump(saved_data, file)

    print("RAG index is ready and saved.")

    return chunks, chunk_vectors, embeddings


# ------------------------------------------------------------
# 4. Calculate similarity between question and chunks
# ------------------------------------------------------------
def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = sum(a * a for a in vec1) ** 0.5
    magnitude2 = sum(b * b for b in vec2) ** 0.5

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product / (magnitude1 * magnitude2)


# ------------------------------------------------------------
# 5. Retrieve the most relevant chunks
# ------------------------------------------------------------
def retrieve_relevant_chunks(question, top_k=4):
    question_vector = embeddings.embed_query(question)

    scored_chunks = []

    for chunk, chunk_vector in zip(chunks, chunk_vectors):
        score = cosine_similarity(question_vector, chunk_vector)
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda x: x[0])

    top_chunks = [chunk for score, chunk in scored_chunks[:top_k]]

    return top_chunks


# ------------------------------------------------------------
# 6. Build/load index when this file starts
# ------------------------------------------------------------
print("Building Companies Act RAG system...")
chunks, chunk_vectors, embeddings = build_simple_index()


# ------------------------------------------------------------
# 7. Set up Ollama LLM and prompt
# ------------------------------------------------------------
llm = ChatOllama(model="llama3.2")

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant answering questions based on the Singapore Companies Act 1967.

Use only the context below to answer the user's question.

Important rules:
1. Do not guess.
2. Do not use outside knowledge.
3. If the answer is not found in the context, say:
"I could not find the answer in the provided Singapore Companies Act 1967 context."
4. If the context contains relevant section numbers, mention them clearly.
5. Explain in plain language, but stay faithful to the Act.

Language rules:
- Answer in the same language as the user's question.
- If the user's question is not in English, answer fully in that language.
- Do not mix languages unless quoting a legal term from the Act is necessary.
- When explaining English legal terms in another language, provide a clear explanation in that language.

Formatting rules:
- Use short paragraphs.
- Use bullet points where helpful.
- Put each bullet point on a new line.
- Leave a blank line between paragraphs.
- Do not put everything into one long paragraph.
- If there are several conditions, list them clearly.
- If there are exceptions or limitations, mention them separately.

Context:
{context}

User's question:
{question}

Answer:
""")



# ------------------------------------------------------------
# 8. Main RAG function
# ------------------------------------------------------------
def translate_question_to_english(question):
    translation_prompt = ChatPromptTemplate.from_template("""
Translate the following question into clear English for legal document search.
Do not answer the question.
Only provide the translated English question.

Question:
{question}

English translation:
""")

    chain = translation_prompt | llm | StrOutputParser()

    translated_question = chain.invoke({
        "question": question
    })

    return translated_question.strip()


def ask_rag(question):
    search_question = translate_question_to_english(question)

    print(f"Original question: {question}")
    print(f"Search question: {search_question}")

    relevant_chunks = retrieve_relevant_chunks(search_question, top_k=4)

    context = "\n\n".join(relevant_chunks)

    chain = prompt | llm | StrOutputParser()

    answer = chain.invoke({
        "context": context,
        "question": question
    })

    return answer
