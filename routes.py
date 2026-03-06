from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from services import get_fitness_plan

# Initialize the router to connect to main.py
router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(request: Request):
    """Member 1: Handled the Home Page route"""
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate")
async def generate(request: Request, goal: str = Form(...), weight: str = Form(...)):
    """Member 2: Handled the Plan Generation route"""
    # This calls the logic from services.py developed by Member 3
    plan = get_fitness_plan(weight, goal)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "plan": plan, 
        "goal": goal
    })
