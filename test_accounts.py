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
        for _ in range(20): 
            self.assertIn(self.__class__.account.get_first_name(), self.__class__.account.first_names)


    def test_get_last_name(self):
        for _ in range(20): 
            self.assertIn(self.__class__.account.get_last_name(), self.__class__.account.last_names)


    def test_get_domain(self):
        for _ in range(20): 
            self.assertIn(self.__class__.account.get_domain(), self.__class__.account.domains)
 
 
    def test_name_extra(self):
        for _ in range(20): 
            self.assertRegex(self.__class__.account.get_name_extra(), r'\d{1,2}')


    def test_get_email_option(self):
        for _ in range(20):
            self.assertLess(self.__class__.account.get_email_option(), 27)

    def test_password(self):
        _min = 8
        _max = 10
        result = self.__class__.account.password(_min, _max)
        self.assertLessEqual(len(result), _max)
        self.assertGreaterEqual(len(result), _min)


    def test_password_throws_exception(self):
        self.assertRaises(ValueError, self.__class__.account.password, 20, 10)


    def test_email_generator_throws_exception(self):
        self.assertRaises(ValueError, self.__class__.account.email_generator, 
            first_name="john", 
            last_name="smith", 
            name_extra="99", 
            domain="google.com", 
            email_option=28)


if __name__ == '__main__':
    unittest.main()