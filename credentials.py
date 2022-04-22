class Credentials:

    '''
        class that generates new instances of credentials
    '''

    credentials_list = []

    def __init__(self,account_name,account_email,account_password):

        self.account_name = account_name
        self.account_email = account_email
        self.account_password = account_password

    def save_account_credentials(self):

        '''
            method saves inputted credentials
        '''

        Credentials.credentials_list.append(self)

    def delete_account_credentials(self):

        '''
            method deletes selected credentials
        '''

        Credentials.credentials_list.remove(self)

       