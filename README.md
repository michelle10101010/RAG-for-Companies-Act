# RAG for Companies Act

A multilingual Retrieval-Augmented Generation (RAG) assistant for the Singapore Companies Act 1967.

This project uses Flask for the web interface, Ollama for the local language model, and Nomic multilingual embeddings for document retrieval.

## Disclaimer

This project is for learning and informational purposes only. It is not legal advice.

Users should refer to the official Singapore Statutes Online version of the Singapore Companies Act 1967 and seek professional advice where necessary.

Please avoid entering confidential client information into the system.

## Features

* Ask questions based on the Singapore Companies Act 1967
* Flask-based web interface
* Local RAG system using Ollama
* Multilingual retrieval experiment using `nomic-embed-text-v2-moe`
* Saved index file for faster loading after the first build
* Chunk size experiment: 2000 characters with 300 overlap
* Curious Bear mascot for a friendly learning interface

## Sample Questions

1. When is the due date for an annual general meeting?
2. When must a company appoint a company secretary?
3. How does a company declare dividend?
4. 根据公司法，公司最少需要多少名董事？
5. Công ty chia cổ tức như thế nào?

## Project Structure

```text
RAG-for-Companies-Act/
├── app.py
├── rag_engine.py
├── test_rag.py
├── requirements.txt
├── README.md
├── .gitignore
├── companies_act_index_nomic-embed-text-v2-moe_chunk2000_overlap300.pkl
├── documents/
├── templates/
└── static/
```

The Singapore Companies Act PDF should be placed inside the `documents/` folder.

The saved index file is:

```text
companies_act_index_nomic-embed-text-v2-moe_chunk2000_overlap300.pkl
```

If this index file is missing or deleted, the system should rebuild it from the PDF inside the `documents/` folder.

## Download the Project

You can download this project from GitHub by clicking:

```text
Code > Download ZIP
```

Then unzip the folder and open it in Terminal, Command Prompt, PowerShell, VS Code Terminal, or Anaconda Prompt.

Alternatively, if you use Git, you may clone the repository:

```bash
git clone <your-repository-url>
cd RAG-for-Companies-Act
```

## Requirements

* Python 3.12 recommended
* Ollama installed and running
* Required Python packages listed in `requirements.txt`
* Singapore Companies Act 1967 PDF placed inside the `documents/` folder

## Companies Act PDF

This project requires the Singapore Companies Act 1967 PDF to be inside the `documents/` folder.

The folder should look like this:

```text
documents/
└── your-companies-act-file.pdf
```

If the PDF is missing, please download the Companies Act 1967 from the official Singapore Statutes Online website and place the PDF inside the `documents/` folder.

## Ollama Setup

This project uses Ollama to run the local language model and embedding model.

Before running the app, install Ollama from the official Ollama website.

Then pull the required models:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text-v2-moe
```

You only need to pull these models once on the same computer.

To check whether the models are already installed, run:

```bash
ollama list
```

You should see `llama3.2` and `nomic-embed-text-v2-moe` in the list.

## Apple / macOS Setup

Open Terminal and go into the project folder.

Example:

```bash
cd /path/to/RAG-for-Companies-Act
```

### Option A: Using normal Python virtual environment on macOS

Create a virtual environment:

```bash
python3 -m venv rag-env
```

Activate the virtual environment:

```bash
source rag-env/bin/activate
```

Install the required packages:

```bash
python3 -m pip install -r requirements.txt
```

Test the RAG engine:

```bash
python3 test_rag.py
```

Run the Flask app:

```bash
python3 app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

### Option B: Using Anaconda on macOS

Create a conda environment:

```bash
conda create -n companies-rag python=3.12
```

Activate the conda environment:

```bash
conda activate companies-rag
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Test the RAG engine:

```bash
python test_rag.py
```

Run the Flask app:

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

## Windows Setup

Windows users may use Command Prompt, PowerShell, VS Code Terminal, or Anaconda Prompt.

If you are new to Python, Anaconda Prompt may be easier because it helps manage Python environments more clearly.

Open your chosen terminal and go into the project folder.

Example:

```bash
cd "C:\path\to\RAG-for-Companies-Act"
```

Quotation marks are recommended if the folder path contains spaces.

### Option A: Using normal Python virtual environment on Windows

Create a virtual environment:

```bash
python -m venv rag-env
```

Activate the virtual environment:

```bash
rag-env\Scripts\activate
```

If the above command does not work in Command Prompt, try:

```bash
rag-env\Scripts\activate.bat
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Test the RAG engine:

```bash
python test_rag.py
```

Run the Flask app:

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

### Option B: Using Anaconda on Windows

Open Anaconda Prompt and go into the project folder.

Example:

```bash
cd "C:\path\to\RAG-for-Companies-Act"
```

Create a conda environment:

```bash
conda create -n companies-rag python=3.12
```

Activate the conda environment:

```bash
conda activate companies-rag
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Test the RAG engine:

```bash
python test_rag.py
```

Run the Flask app:

```bash
python app.py
```

Then open your browser and go to:

```text
http://127.0.0.1:5000
```

## Running the Project Again Later

The environment only needs to be created once.

After the first setup, you do not need to create the environment again.

### If using Anaconda

Open Terminal or Anaconda Prompt, go into the project folder, then run:

```bash
conda activate companies-rag
python app.py
```

If your macOS setup uses `python3`, run:

```bash
conda activate companies-rag
python3 app.py
```

### If using normal Python virtual environment on macOS

Open Terminal, go into the project folder, then run:

```bash
source rag-env/bin/activate
python3 app.py
```

### If using normal Python virtual environment on Windows

Open Command Prompt, PowerShell, or VS Code Terminal, go into the project folder, then run:

```bash
rag-env\Scripts\activate
python app.py
```

Then open the local Flask link shown in the terminal, usually:

```text
http://127.0.0.1:5000
```

## How the Saved Index Works

This project uses a saved index file for document retrieval.

The saved index file is:

```text
companies_act_index_nomic-embed-text-v2-moe_chunk2000_overlap300.pkl
```

If the index file already exists, the app should load it for faster retrieval.

If this file is missing, the system should rebuild it from the PDF inside the `documents/` folder.

The first rebuild may take some time.

If the index file is deleted, the system should recreate it again on the next run.

## Quick Test Checklist

Before running the app, check the following:

1. The project folder has been downloaded or cloned.
2. The Companies Act PDF is inside the `documents/` folder.
3. Python environment has been created and activated.
4. Python packages have been installed using `pip install -r requirements.txt`.
5. Ollama is installed and running.
6. The required Ollama models have been downloaded.
7. `python test_rag.py` runs successfully.
8. `python app.py` starts the Flask app successfully.
9. The browser opens `http://127.0.0.1:5000`.

## Troubleshooting

### 1. `pip install -r requirements.txt` does not work

Make sure your Python environment is activated first.

For Anaconda users:

```bash
conda activate companies-rag
```

For macOS virtual environment users:

```bash
source rag-env/bin/activate
```

For Windows virtual environment users:

```bash
rag-env\Scripts\activate
```

Then try again:

```bash
pip install -r requirements.txt
```

### 2. Ollama connection error

Make sure Ollama is installed and running.

You can check whether Ollama is available by running:

```bash
ollama --version
```

You can check installed models by running:

```bash
ollama list
```

If the required models are missing, run:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text-v2-moe
```

### 3. Model not found

Run:

```bash
ollama pull llama3.2
ollama pull nomic-embed-text-v2-moe
```

Then run the app again.

### 4. Companies Act PDF not found

Make sure the Singapore Companies Act 1967 PDF is inside the `documents/` folder.

The folder should look like this:

```text
documents/
└── your-companies-act-file.pdf
```

### 5. Saved index file is missing

This may happen on a fresh GitHub download.

The app should automatically create the saved index file on first run.

If it does not, run:

```bash
python test_rag.py
```

or on macOS:

```bash
python3 test_rag.py
```

### 6. Port 5000 is already in use

Another Flask app may already be running.

Close the other app, or change the port number inside `app.py`.

For example:

```python
app.run(debug=True, port=5001)
```

Then open:

```text
http://127.0.0.1:5001
```

### 7. The first answer is slow

The first run may take longer because the saved index may need to be created from the PDF.

After the index is created, future runs should be faster.

### 8. `python` command does not work

On macOS, try:

```bash
python3 --version
```

Then use `python3` instead of `python`.

On Windows, make sure Python has been installed and added to PATH, or use Anaconda Prompt.

### 9. `conda` command does not work

If `conda` is not recognised, Anaconda or Miniconda may not be installed or may not be added to PATH.

You may use the normal Python virtual environment method instead, or open Anaconda Prompt if Anaconda is installed.

## Notes

* This version uses the Nomic multilingual embedding model.
* This version uses a saved `.pkl` index file instead of a FAISS index folder.
* The saved index file is `companies_act_index_nomic-embed-text-v2-moe_chunk2000_overlap300.pkl`.
* The saved index file was built using chunk size 2000 and overlap 300.
* If the index file is deleted, the system should rebuild it from the PDF in the `documents/` folder.
* The first rebuild may take some time.
* The assistant answers based on the retrieved Singapore Companies Act 1967 document context.
* This project is for learning and experimentation. It is not legal advice.
* Please avoid entering confidential client information into the system.

## Author

Created by Michelle / Curious Bear.

## Special Thanks

* My human teacher, Mr. Go Figure Out, for his guidance and encouragement.
* My AI teacher, ChatGPT, for guidance.
