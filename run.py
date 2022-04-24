from user import User
from credentials import Credentials
import unittest


def create_account(acc_name, acc_email, acc_password):
    
    '''
        method to create an account
    '''

    new_credentials = Credentials(acc_name, acc_email, acc_password)
    return new_credentials


def save_account():
    '''
        method to save account
    '''

    Credentials.save_account_credentials()

def delete_account():

    '''
        method to deleter an account
    '''

    Credentials.delete_account_credentials()

def display_accounts():

    '''
        Function that returns all saved accounts
    '''

    Credentials.display_accounts()

def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new account, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print ("Account name ....")
                            acc_name = input()

                            print("Email ...")
                            acc_email = input()

                            print("Password...")
                            acc_password = input()


                            save_account(create_account()) # create and save new contact.
                            print ('\n')
                            print(f"New Account {acc_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_accounts():
                                    print("Here is a list of all your accounts")
                                    print('\n')

                                    for accounts in display_accounts():
                                            print(f"{Credentials.account_name} {Credentials.account_email} .....")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')


                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")




if __name__ == '__main__':
    unittest.main()