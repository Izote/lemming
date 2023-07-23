import os
from dotenv import load_dotenv


load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

URL = os.environ.get("URL")
KEY = os.environ.get("KEY")
