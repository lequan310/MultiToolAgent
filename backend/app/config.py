import os
from dotenv import load_dotenv

load_dotenv()

if not os.getenv("DOCKER_ENV"):
    os.environ["QDRANT_HOST"] = "localhost"
    os.environ["API_HOST"] = "localhost"
