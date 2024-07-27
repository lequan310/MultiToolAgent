from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routes.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router, prefix="/chat")


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
