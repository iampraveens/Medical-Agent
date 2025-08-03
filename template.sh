echo "Creating project structure..."
mkdir -p src
mkdir -p research
mkdir -p data

touch src/__init__.py
touch src/helpers.py
touch src/prompts.py
touch research/experiments.ipynb
touch research/trials.ipynb
touch .env
touch setup.py
touch app.py
touch requirements.txt

echo "Project structure created successfully."
echo "Remember to fill in the necessary details in the .env, setup.py, and requirements.txt files."