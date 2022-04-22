class User:
    """
    Class that generates new instances of accounts.
    """
    
    user_accounts = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_account_details(self):

        '''
        save_account_details method saves account details inserted by the user.
        '''

        User.user_accounts.append(self)

    def delete_account_details(self):

        '''
        delete_account_details method deletes the account details selected
        '''

        User.delete_account_details.remove(self)

    @classmethod
    def display_accounts(cls):
        
