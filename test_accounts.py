import unittest
import accounts

class TestAccounts(unittest.TestCase):
    account = accounts.Accounts()

    def test_email_generator(self):
        result = self.__class__.account.email_generator(
            first_name="john", 
            last_name="smith", 
            name_extra="99", 
            domain="google.com", 
            email_option=0
        )
        self.assertEqual(result, "johnsmith99@google.com")


    def test_get_first_name(self):
       result = self.__class__.account.get_first_name()
       self.assertIn(result, self.__class__.account.first_names)


    def test_get_last_name(self):
       result = self.__class__.account.get_last_name()
       self.assertIn(result, self.__class__.account.last_names)


    def test_get_domain(self):
       result = self.__class__.account.get_domain()
       self.assertIn(result, self.__class__.account.domains)
 
 
    def test_name_extra(self):
        result = self.__class__.account.get_name_extra()
        self.assertRegex(result, r'\d{1,2}')


    def test_get_email_option(self):
        result = self.__class__.account.get_email_option()
        self.assertLess(result, 27)


if __name__ == '__main__':
    unittest.main()