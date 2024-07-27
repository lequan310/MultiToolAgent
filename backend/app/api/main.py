import uvicorn
from app.config import os


if os.getenv("DOCKER_ENV") == "true":
    HOST = os.getenv("API_HOST")
else:
    HOST = "localhost"

PORT = int(os.getenv("API_PORT"))


def run():
    uvicorn.run("app.api.app:app", host=HOST, port=PORT, reload=True)


if __name__ == "__main__":
    run()
