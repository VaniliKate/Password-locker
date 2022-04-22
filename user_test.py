import unittest #imports unittest module
from user import User #imports the User class
import pyperclip

class TestUser (unittest.TestCase):

     '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases

    '''

def setUp(self):

    '''
        Set up method to run before each test cases.
    '''

    self.new_user = User("Kate Vanili", "Same#3030") # create user detail objects

def test_init(self):

    '''
        test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.username,"Kate Vanili")
    self.assertEqual(self.new_user.password,"Same#3030")

def tearDown(self):

    '''
            tearDown method that does clean up after each test case has run.
    '''

    User.user_accounts = []

def test_save_user_details(self):

    '''
        test_save_account_details test case to test if the user account details object is saved into
         the user_accounts list
    '''

    self.new_user.save_user_details()  #saves new user details
    self.assertEqual(len(User.user_accounts),1)

def test_delete_user_details(self):

    '''
        test_delete_user_details test case to test if the user account details can be deleted from
         the user_accounts list
    '''

    self.new_user.save_user_details()  
    test_user = User("Kate Vanili", "Same#3030")
    test_user.save_user_details()

    self.new_user.delete_user_details()  #deletes user details
    self.assertEqual(len(User.user_accounts),1)

#def test_find_account_by_username(self):
    #'''
        #test to check if we can find an account by username and display information
    #'''

    #self.new_user.save_user_details()  
    #test_user = User("Kate Vanili", "Same#3030")
    #test_user.save_user_details()

    #found_account = User.find_by_username("Kate Vanili")

    #@classmethod
    #def find_by_username(cls,username):
         #'''
        #Method that takes in a username and returns an account that matches that username.

        #Args:
            #username: Username to search for
       # Returns :
            #Account that matches the username.
        #'''

        #for user_account in cls.user_accounts:
            #if user_accounts.username === username:
                #return user_account
        


if __name__ == '__main__':
    unittest.main()


