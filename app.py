import os
import google.generativeai as genai
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load environment variables from your .env file
load_dotenv()

# --- Configuration ---
app = Flask(__name__)

# Configure the Google AI SDK with your secret API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# --- The Main Route ---
@app.route('/', methods=['GET', 'POST'])
def home():
    recipe = None

    # This block runs when the user submits the form
    if request.method == 'POST':
        try:
            ingredients = request.form['ingredients']
            
            # This is the detailed instruction for the AI model
            prompt = f"""
            You are a creative and experienced chef. 
            Your task is to create a delicious recipe based ONLY on the ingredients provided, plus common pantry staples like oil, salt, pepper, and water.
            
            Please provide a unique, catchy name for the recipe as a main heading.
            Then, list the necessary ingredients under an "Ingredients" subheading.
            Finally, provide clear, step-by-step cooking instructions under an "Instructions" subheading.
            
            Ensure the recipe is easy to follow for a home cook.

            Ingredients provided: {ingredients}
            """
            
            # Select the AI model and generate the recipe
            model = genai.GenerativeModel('models/gemini-flash-latest')
            response = model.generate_content(prompt)
            recipe = response.text

        except Exception as e:
            # Print the error to the terminal for debugging
            print(f"AN ERROR OCCURRED: {e}")
            # Show a user-friendly error message on the webpage
            recipe = "Sorry, an error occurred while generating the recipe. Please check the terminal for details."
            
    # Render the webpage, passing in the recipe if it exists
    return render_template('index.html', recipe=recipe)


# This allows the script to be run directly
if __name__ == '__main__':
    app.run(debug=True)