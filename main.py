from fastapi import FastAPI
from routes import router

app = FastAPI()

# This connects the routes created by your "team members"
app.include_router(router)

if _name_ == "_main_":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True
