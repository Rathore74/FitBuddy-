import os
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from google import genai

app = FastAPI()

# This tells FastAPI where to find your HTML files
templates = Jinja2Templates(directory="templates")

# Initialize Gemini Client
# Note: You will need to set your API Key in your environment later
client = genai.Client()

@app.get("/")
async def home(request: Request):
    """Shows the initial form to the user."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate")
async def generate_plan(request: Request, goal: str = Form(...), weight: str = Form(...)):
    """Sends user data to Gemini and displays the result."""
    
    prompt = f"Create a simple 3-day fitness and meal plan for a person who weighs {weight}kg. Goal: {goal}."
    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
        ai_result = response.text
    except Exception as e:
        ai_result = f"Error: Could not connect to AI. {str(e)}"

    return templates.TemplateResponse("index.html", {
        "request": request, 
        "plan": ai_result,
        "goal": goal
    })
