from google import genai
import os

# Initialize the Gemini Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def get_fitness_plan(weight, goal):
    """
    Using 'flash-lite' and a shorter prompt to avoid the 429 error.
    """
    # Shortening the prompt reduces "Token" usage
    prompt = f"Give a quick 3-day workout and meal plan for {weight}kg. Goal: {goal}. Be very brief."
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-lite", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        if "429" in str(e):
            return "The AI is currently busy. Please wait 1 minute and click only once."
        return f"AI Service Error: {str(e)}"
