class User:
    user_accounts = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_account_details(self):
        