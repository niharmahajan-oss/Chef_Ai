ChefAI 🧑‍🍳
A smart, AI-powered recipe generator that creates unique recipes from the ingredients you have on hand. Built with Python, Flask, and the Google Gemini API.

(Note: Take a screenshot of your running app and replace the placeholder path above. An animated GIF of the app working is even better!)

## Features
Dynamic Recipe Generation: Get unique, creative recipes based on any list of ingredients.

AI-Powered Core: Utilizes Google's advanced Gemini model (gemini-flash-latest) to understand and generate human-like recipe instructions.

Minimalist UI: A clean, simple, and responsive user interface built with HTML and CSS.

Full-Stack Application: Demonstrates a complete end-to-end web application flow from front-end to back-end to an external API.

## Tech Stack
Backend: Python, Flask

AI Model: Google Gemini API (google-generativeai)

Frontend: HTML5, CSS3

## Project Setup and Installation
To run this project locally, follow these steps.

### 1. Prerequisites
Before you begin, make sure you have the following files in your project directory.

.gitignore: This file is crucial to prevent sensitive data and unnecessary files from being uploaded to GitHub. Create a file named .gitignore and add the following lines:

# Virtual Environment
venv/

# Environment Variables
.env
requirements.txt: This file lists all the Python libraries your project needs. Create it by running this command in your active virtual environment:

Bash

pip freeze > requirements.txt
### 2. Installation Steps
Clone the repository:

Bash

git clone https://github.com/your-username/chefai.git
cd chefai
(Replace your-username with your actual GitHub username.)

Create and activate a virtual environment:

Bash

# Create the virtual environment
python -m venv venv

# Activate on macOS/Linux
source venv/bin/activate

# Activate on Windows
# venv\Scripts\activate
Install the required dependencies:

Bash

pip install -r requirements.txt
Set up your API Key:

Create a file named .env in the root of your project folder.

Inside the .env file, add your API key like this:

GOOGLE_API_KEY=YOUR_API_KEY_HERE
(Get your free key from Google AI Studio).

Run the application:

Bash

python app.py
The application will be running at http://127.0.0.1:5000.

## How to Use
Simply open the web application in your browser, type the ingredients you have (separated by commas) into the text box, and click the "Generate Recipe" button. The AI will generate and display a new recipe for you.
