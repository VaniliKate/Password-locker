import unittest  # imports unittest module
from user import User  # imports the User class



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

        # create user detail objects
        self.new_user = User("Kate Vanili", "Same#3030")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username, "Kate Vanili")
        self.assertEqual(self.new_user.password, "Same#3030")

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

        self.new_user.save_user_details()  # saves user details
        self.assertEqual(len(User.user_accounts), 1)

    def test_delete_user_details(self):

        '''
            test_delete_user_details test case to test if the user account details can be deleted from
            the user_accounts list
        '''

        self.new_user.save_user_details()
        test_user = User("Kate Vanili","Same#3030")
        test_user.save_user_details()

        self.new_user.delete_user_details() #deletes user details
        self.assertEqual(len(User.user_accounts),1)

    def test_display_all_users(self):

        '''
            method that returns a list of all accounts saved
        '''

        self.assertEqual(User.display_accounts(),User.user_accounts)

    

        





    

    


if __name__ == '__main__':
    unittest.main()
