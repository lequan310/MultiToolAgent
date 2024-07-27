from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.routes.chat import router as chat_router


app = FastAPI()

app.include_router(chat_router, tags=["Chat"], prefix="/chat")


@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Hello World"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
