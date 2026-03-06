from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from services import get_fitness_plan

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def home(request: Request):
    """Shows the home page"""
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate")
async def generate(request: Request, goal: str = Form(...), weight: str = Form(...)):
    """Triggers the AI service and returns the result"""
    plan = get_fitness_plan(weight, goal)
    return templates.TemplateResponse("index.html", {
        "request": request, 
        "plan": plan, 
        "goal": goal
    })
