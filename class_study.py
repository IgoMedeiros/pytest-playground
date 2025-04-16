class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username: str, email: str):
        if username in self.users:
            raise ValueError('User exists!')
        
        self.users[username] = email
        return True
    
    def get_user(self, username: str):
        return self.users.get(username)