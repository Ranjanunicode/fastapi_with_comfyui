import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

SAVE_IMAGE_WEBSOCKET = os.getenv("SAVE_IMAGE_WEBSOCKET")
SERVER_ADDERESS = os.getenv("SERVER_ADDERESS")