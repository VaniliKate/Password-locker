class User:
    """
    Class that generates new instances of accounts.
    """
    
    user_accounts = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_user_details(self):

        '''
        save_user_details method saves account details inserted by the user.
        '''

        User.user_accounts.append(self)

    def delete_user_details(self):

        '''
        delete_user_details method deletes the account details selected
        '''

        User.user_accounts.remove(self)
        

    @classmethod
    def display_accounts(cls):

        '''
            display_accounts method will display account details when called
        '''

        return cls.user_accounts

    
