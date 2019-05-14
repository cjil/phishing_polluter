import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import unittest
import accounts
import json
class TestAccounts(unittest.TestCase):

    def setUp(self):
        self.john = accounts.Account(
            first_names=["John"], 
            last_names=["Smith"], 
            domains=["google.com"],
            email_option=0)
        self.account = accounts.Account()

    
    def tearDown(self):
        pass


    def test_set_email_address(self):
        self.assertRegex(self.john.set_email_address(email_option=0), r'johnsmith\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=1), r'jsmith\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=2), r'johns\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=3), r'sjohn\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=4), r'smithj\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=5), r'smithjohn\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=6), r'john\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=7), r'smith\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=8), r'johnsmith@google.com')
        self.assertRegex(self.john.set_email_address(email_option=9), r'jsmith@google.com')
        self.assertRegex(self.john.set_email_address(email_option=10), r'johns@google.com')
        self.assertRegex(self.john.set_email_address(email_option=11), r'sjohn@google.com')
        self.assertRegex(self.john.set_email_address(email_option=12), r'smithj@google.com')
        self.assertRegex(self.john.set_email_address(email_option=13), r'smithjohn@google.com')
        self.assertRegex(self.john.set_email_address(email_option=14), r'john@google.com')
        self.assertRegex(self.john.set_email_address(email_option=15), r'smith@google.com')
        self.assertRegex(self.john.set_email_address(email_option=16), r'john.smith\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=17), r'j.smith\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=18), r'john.s\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=19), r's.john\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=20), r'smith.j\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=21), r'smith.john\d{1,2}@google.com')
        self.assertRegex(self.john.set_email_address(email_option=22), r'john.smith@google.com')
        self.assertRegex(self.john.set_email_address(email_option=23), r'j.smith@google.com')
        self.assertRegex(self.john.set_email_address(email_option=24), r'john.s@google.com')
        self.assertRegex(self.john.set_email_address(email_option=25), r's.john@google.com')
        self.assertRegex(self.john.set_email_address(email_option=26), r'smith.j@google.com')
        self.assertRegex(self.john.set_email_address(email_option=27), r'smith.john@google.com')
        with self.assertRaises(ValueError):
            self.john.set_email_address(email_option=28)


    def test_first_name(self):
        with open('first_names.json') as f:
            first_names = [r.lower() for r in json.loads(f.read())]
        self.assertEqual(self.account.first_name, self.account.first_name)
        self.assertEqual(self.john.first_name, "john")
        self.assertIn(self.account.first_name, first_names)


    def test_last_name(self):
        with open('last_names.json') as f:
            last_names = [r.lower() for r in json.loads(f.read())]
        self.assertEqual(self.account.last_name, self.account.last_name)
        self.assertEqual(self.john.last_name, "smith")
        self.assertIn(self.account.last_name, last_names)


    def test_domain(self):
        with open('domains.json') as f:
            domains = [r.lower() for r in json.loads(f.read())]
        self.assertEqual(self.account.domain, self.account.domain)
        self.assertEqual(self.john.domain, "google.com")        
        self.assertIn(self.account.domain, domains)
 
 
    def test_name_extra(self):
        self.assertRegex(self.account.name_extra, r'\d{1,2}')
        self.assertEqual(type(self.account.name_extra), str)


    def test_email_option(self):
        for _ in range(100):
            self.assertLess(self.account.set_email_option(), 27)


    def test_set_password(self):
        min_length = 8
        max_length = 12
        result = self.account.set_password(min_length=min_length, max_length=max_length)
        self.assertLessEqual(len(result), max_length)
        self.assertGreaterEqual(len(result), min_length)
        with self.assertRaises(ValueError):
            self.account.set_password(min_length=20, max_length=10)


if __name__ == '__main__':
    unittest.main()
