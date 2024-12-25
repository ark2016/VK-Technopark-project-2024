from fastapi import FastAPI
from app.routers.questions import router

# uvicorn main:app --reload
app = FastAPI(
    title="VK-course-work",
    version="0.0.1",
)

app.include_router(router)
