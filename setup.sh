#!/bin/bash

# Clone repository (if not already cloned)
# git clone https://github.com/YOUR_USERNAME/tds-llm-api.git
# cd tds-llm-api

# Create directory structure
mkdir -p api utils

# Create core files
touch api/__init__.py api/main.py
touch utils/__init__.py utils/colab_parser.py utils/llm_handler.py
touch requirements.txt vercel.json .gitignore .env

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
# Clone repository
git clone https://github.com/YOUR_USERNAME/tds-llm-api.git
cd tds-llm-api

# Create project structure
mkdir -p api utils
touch api/main.py utils/colab_parser.py utils/llm_handler.py
touch requirements.txt vercel.json .gitignore

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install packages
pip install -r requirements.txt
uvicorn api.main:app --reload

#deployment
npm install -g vercel

#push
git add .
git commit -m "Full working version with deployment setup"
git push origin main

chmod +x setup.sh
