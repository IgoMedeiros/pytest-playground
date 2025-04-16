import requests

class APIClient:
    def user_get_data(self, user_id):
        response = requests.get(f"https://api.example.com/users/{user_id}")
        if response.status_code == 200:
            return response.json()
        raise ValueError('API request failed')
    
class UserService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_username(self, user_id):
        user_data = self.api_client.user_get_data(user_id)
        return user_data['name'].upper()