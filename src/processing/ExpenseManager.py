from src.entities.user import User


class ExpenseManager:
    def __init__(self):
        self.users = {}



    def create_user(self, username, password):
        if username not in self.users:
           u = User(username, password)
           self.users[username] = u

           





    

