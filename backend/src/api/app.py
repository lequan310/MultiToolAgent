from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api.routes.files import router as file_router

app = FastAPI()

app.include_router(file_router, prefix="/files")


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
