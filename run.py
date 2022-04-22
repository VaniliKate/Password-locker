from user import User
from credentials import Credentials

def create_account(acc_name,acc_email,acc_password):

    '''
        method to create an account
    '''

    new_credentials = Credentials(acc_name, acc_email, acc_password)
    return new_credentials

def save_account(credentials):
    
    '''
        method to save account
    '''

    credentials.save_account_credentials()

