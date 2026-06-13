# RAG for Companies Act

A multilingual Retrieval-Augmented Generation (RAG) assistant for the Singapore Companies Act 1967.

This project uses Flask for the web interface, Ollama for the local language model, and Nomic multilingual embeddings for document retrieval.

## Features

* Ask questions based on the Singapore Companies Act 1967
* Flask-based web interface
* Local RAG system using Ollama
* Multilingual retrieval experiment using `nomic-embed-text-v2-moe`
* Saved index file for faster loading after the first build
* Chunk size experiment: 2000 characters with 300 overlap

## Project Structure

```text
RAG-for-Companies-Act/
├── app.py
├── rag_engine.py
├── test_rag.py
├── requirements.txt
├── README.md
├── companies_act_index_nomic-embed-text-v2-moe_chunk2000_overlap300.pkl
├── documents/
├── templates/
└── static/
```

## Requirements

* Python 3.x
* Ollama installed
* Required Python packages listed in `requirements.txt`

## Ollama Models

Pull the required models before running the app:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text-v2-moe
```

## Install Python Dependencies

```bash
pip install -r requirements.txt
```

## How to Run

### Step 1: Start Ollama

Open a terminal and run:

```bash
ollama serve
```

If Ollama is already running, you may see a message that the port is already in use. That is fine.

### Step 2: Test the RAG Engine

In the project folder, run:

```bash
python test_rag.py
```

This checks whether the RAG engine can load the index and answer a test question.

### Step 3: Run the Flask App

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

## Notes

* This version uses the Nomic multilingual embedding model.
* The saved index file was built using chunk size 2000 and overlap 300.
* If the index file is deleted, the system will rebuild it from the PDF in the `documents/` folder.
* The first rebuild may take some time.
* Please avoid entering confidential client information into the system.

## Author

Created by Michelle / Curious Bear.
