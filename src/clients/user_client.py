import requests
from src.errors.errors import Unauthorized, Forbidden, BadRequest, PreconditionFailed
import os

class UserClient:
    def __init__(self, token):
        self.token = token
        self.user_path = os.environ.get('USERS_PATH')

    def validate_user(self):
        url = self.user_path + "/users/me"
        headers = {"Authorization": self.token}
        response = requests.get(url, headers=headers)
        
        if response.status_code == 401:
            raise Unauthorized()
        
        if response.status_code == 403:
            raise Forbidden()
        
        if response.status_code == 400:
            raise BadRequest()
        
        if response.status_code == 412:
            raise PreconditionFailed()
        
        json_data = response.json()
        return json_data.get('id')
         
