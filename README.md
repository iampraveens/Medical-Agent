# 🏥 Medical Agent

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/) [![Flask](https://img.shields.io/badge/flask-3.0%2B-black.svg)](https://flask.palletsprojects.com/) [![LangChain](https://img.shields.io/badge/langchain-0.3%2B-orange.svg)](https://www.langchain.com/) [![Pinecone](https://img.shields.io/badge/pinecone-7.2%2B-brightgreen.svg)](https://www.pinecone.io/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](../../issues)

A **Retrieval-Augmented Generation (RAG)**-based medical assistant powered by **LangChain, Google Generative AI, and Pinecone**. This project is designed to answer medical-related queries using information retrieved from the **Gale Encyclopedia of Medicine (3rd Edition)**, providing clear, empathetic, and professional responses.

---

## ✨ Key Features

- **Medical Question Answering**: Retrieves trusted information from medical documents and generates accurate answers.
- **RAG Pipeline**: Combines document retrieval with LLM inference for precise and context-aware responses.
- **Flask Web Interface**: User-friendly chatbot interface for querying medical knowledge.
- **Vector Search**: Uses **Pinecone** as a scalable vector database for efficient document retrieval.
- **Custom Prompts**: Tailored medical prompt ensuring empathy, clarity, and reliability.
- **Docker/Deployment Ready**: Includes `Procfile` for deployment (e.g., Heroku, Render).

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/iampraveens/medical-agent.git
cd medical-agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Create a `.env` file in the project root and add the following:

```env
GEMINI_API_KEY=your_google_genai_api_key
PINECONE_API_KEY=your_pinecone_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGSMITH_PROJECT=medical-agent
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

### 5. Run the Application

```bash
python app.py
```

Access the app at [**http://127.0.0.1:5555**](http://127.0.0.1:5555).

---

## 🚀 Usage

1. Open the web app in your browser.
2. Type a medical question (e.g., _"What is Acromegaly and how is it treated?"_).
3. The assistant retrieves context from the medical encyclopedia and provides a concise, empathetic response.

Example JSON request (API mode):

```bash
curl -X POST http://127.0.0.1:5555/get_response \
     -H "Content-Type: application/json" \
     -d '{"message": "What is Diabetes?"}'
```

Response:

```json
{
  "response": "Diabetes is a metabolic disorder characterized by high blood sugar levels..."
}
```

---

## 📂 Project Structure

```
medical-agent/
├── app.py                 # Flask web server entrypoint
├── requirements.txt       # Python dependencies
├── setup.py               # Package setup configuration
├── Procfile               # Deployment process definition
├── LICENSE                # MIT License
├── config/                # Configuration files
│   └── settings.py        # Global settings & API keys
├── data/                  # Medical documents (PDFs)
├── research/              # Jupyter notebooks for experiments
├── src/                   # Core source code
│   ├── chain.py           # Document & retrieval chain setup
│   ├── document_loader.py # PDF loading & preprocessing
│   ├── embeddings.py      # Embedding model initialization
│   ├── execute_vector_store.py # Pipeline to build vector store
│   ├── llm_inference.py   # LLM inference functions
│   ├── prompts.py         # Medical-specific prompts
│   ├── retrieval.py       # Retriever setup
│   ├── text_processing.py # Text splitting & preprocessing
│   └── vector_store.py    # Pinecone vector store utilities
├── static/                # Frontend assets (CSS/JS)
├── templates/             # Flask HTML templates
│   ├── index.html         # Chatbot UI
│   └── base.html          # Layout template
└── template.sh            # Shell script to bootstrap structure
```

---

## 📚 Dependencies

- [LangChain](https://www.langchain.com/)
- [Google Generative AI](https://ai.google/)
- [Pinecone](https://www.pinecone.io/)
- [Sentence-Transformers](https://www.sbert.net/)
- [Flask](https://flask.palletsprojects.com/)
- [PyPDF](https://pypi.org/project/pypdf/)
- [Python-Dotenv](https://pypi.org/project/python-dotenv/)

---

## 🤝 Contribution Guidelines

Contributions are welcome! Please follow these steps:

1. **Fork** the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Added new feature'`
4. Push branch: `git push origin feature-name`
5. Submit a **Pull Request**.

---

## 📜 License

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Developed with ❤️ by **Praveen S** ([GitHub](https://github.com/iampraveens))
