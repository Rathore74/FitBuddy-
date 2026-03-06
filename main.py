from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes import router

app = FastAPI()

# Mount the static folder for CSS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include the routes developed by the team
app.include_router(router)

if _name_ == "_main_":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
