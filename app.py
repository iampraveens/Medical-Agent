from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, render_template, request, jsonify
from src.embeddings import get_embeddings
from src.retrieval import load_existing_vector_store, create_retriever
from src.llm_inference import get_chat_model
from src.prompts import get_medical_prompt
from src.chain import create_document_chain, create_full_retrieval_chain
from config.settings import Config

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")


app = Flask(__name__)

config = Config()
embeddings = get_embeddings()
vector_store = load_existing_vector_store(config.PINECONE_INDEX_NAME, embeddings)
retriever = create_retriever(vector_store, k=config.RETRIEVAL_K)
llm = get_chat_model(config.CHAT_MODEL)
prompt = get_medical_prompt()
document_chain = create_document_chain(llm, prompt)
retrieval_chain = create_full_retrieval_chain(retriever, document_chain)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        if not user_message:
            return jsonify({'response': 'Please provide a valid message.'}), 400

        # Run retrieval chain
        response = retrieval_chain.invoke({
            "input": user_message
        })
        return jsonify({'response': response['answer']})
    except Exception as e:
        return jsonify({'response': f'Error processing request: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)