#!/bin/bash

# Ensure the script is executable
# Run: chmod +x setup_and_run.sh

# Step 1: Set up Python virtual environment
echo "Setting up Python virtual environment..."
python3 -m venv castela

# Activate the virtual environment
echo "Activating virtual environment..."
source castela/bin/activate

# Step 2: Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install transformers torch flask beautifulsoup4 requests

# Step 3: Run the Flask server
echo "Starting Flask server..."
python app.py

