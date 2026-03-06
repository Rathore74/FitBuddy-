from google import genai
client = genai.Client()

def get_fitness_plan(weight, goal):
    prompt = f"Create a 3-day workout and meal plan for weight {weight}kg. Goal: {goal}."
    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return response.text
