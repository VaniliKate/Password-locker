class User:
    """
    Class that generates new instances of contacts.
    """
    
    user_accounts = []

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_account_details(self):

        '''
        save_contact method saves contact objects into contact_list
        '''
