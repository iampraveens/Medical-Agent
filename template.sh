echo "Creating project structure..."
mkdir -p src
mkdir -p research
mkdir -p data
mkdir -p config
mkdir -p templates
mkdir -p static

touch src/__init__.py
touch src/document_loader.py
touch src/text_processing.py
touch src/embeddings.py
touch src/vector_store.py
touch src/execute_vector_store.py
touch src/retrieval.py
touch src/llm_inference.py
touch src/prompts.py
touch src/chain.py
touch research/experiments.ipynb
touch research/trials.ipynb
touch config/settings.py
touch config/__init__.py
touch templates/index.html
touch templates/base.html
touch static/style.css
touch static/script.js
touch .env
touch setup.py
touch app.py
touch requirements.txt

echo "Project structure created successfully."
echo "Remember to fill in the necessary details in the .env, setup.py, and requirements.txt files."