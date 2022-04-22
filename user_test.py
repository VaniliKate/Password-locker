import unittest #imports unittest module
from user import User #imports the User class


class TestUser(unittest.TestCase):

    '''
        Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):

        '''
            method to run before each test case
        '''

        self.new_user = User("Kate Vanili","Same#3030")#create user detail objects

    

        

   



    



