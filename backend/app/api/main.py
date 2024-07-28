import uvicorn
from app.config import os


def run():
    uvicorn.run(
        "app.api.app:app",
        host=os.getenv("API_HOST"),
        port=int(os.getenv("API_PORT")),
        reload=True,
    )


if __name__ == "__main__":
    run()
