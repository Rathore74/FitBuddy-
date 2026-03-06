from google import genai

# Initialize the Gemini Client
client = genai.Client()

def get_fitness_plan(weight, goal):
    """
    This function handles the AI generation logic.
    Separating this into services.py shows professional modular design.
    """
    prompt = f"Create a detailed 3-day workout and meal plan for someone weighing {weight}kg with the goal: {goal}."
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Service Error: {str(e)}"
