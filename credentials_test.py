import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    '''
        Test class to test for the credentials behaviours
    '''

    def setUp(self):
        '''
            method to run before each test case
        '''

        self.new_account = Credentials(
            "Twitter", "test@gmail.com", "Amy80=34#")

    def test_init(self):
        '''
            to test if the object is initialized correctly
        '''

        self.assertEqual(self.new_account.account_name, "Twitter")
        self.assertEqual(self.new_account.account_email, "test@gmail.com")
        self.assertEqual(self.new_account.account_password, "Amy80=34#")

    def tearDown(self):
        '''
            the method cleans up after each test run
        '''
        Credentials.credentials_list = []

    def test_save_credentials(self):
        '''
            check if credential objects are saved to the list
        '''

        self.new_account.save_account_credentials()  # saves new credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_delete_credentials(self):
        '''
        check if credentials are deleted
        '''

        self.new_account.save_account_credentials()
        test_credentials = Credentials("Twitter", "test@gmail.com", "Asmh?2@v")
        test_credentials.save_account_credentials()

        self.new_account.delete_account_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def display_accounts(self):
        '''
            check for list of accounts
        '''

        self.assertEqual(Credentials.display_accounts(),
                         Credentials.credentials_list)


if __name__ == '__main__':
    unittest.main()
