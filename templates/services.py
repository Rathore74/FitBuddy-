from google import genai

client = genai.Client()

def get_fitness_plan(weight, goal):
    """Generates the AI content"""
    prompt = f"Create a 3-day workout and meal plan for a weight of {weight}kg. Goal: {goal}."
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI Service Error: {str(e)}"
