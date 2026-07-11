import requests
from dotenv import load_dotenv
import os



load_dotenv()

class Router:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")

    def register_user(self, username, password):
        data = {
            "username": username,
            "password": password
        }

        response = requests.post(
            f"{self.base_url}/users/register",
            json=data
        )

        return response