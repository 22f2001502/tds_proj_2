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
chmod +x setup.sh
