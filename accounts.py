import os
import secrets
import string
from fake_useragent import UserAgent


class Accounts():
    """Accounts

    Variables:
        first_names
        last_names
        domains
        chars
    Methods:
        email()
        email_generator(first_name, last_name, name_extra, domain)
        password(min, max)
    """


    def __init__(self, first_names, last_names, domains):
        """Initialise the class

        Keyword arguments:
        
        first_names LIST    First names
        last_names LIST     Last names
        domains LIST        Domain names
        """
        self.first_names = first_names
        self.last_names = last_names
        self.domains = domains
        self.chars = f'{string.ascii_letters}{string.digits}!@#$%^&*()'
        self.ua = UserAgent()


    def email(self):
        """Generate random first_name, last_name, domain name and name
        extra using the first_names, last_names, domain_names lists and
        a random integer.
        
        Return a random email address 
        """
        random_choice = secrets.SystemRandom().choice
        first_name = random_choice(self.first_names).lower()
        last_name = random_choice(self.last_names).lower()
        domain = random_choice(self.domains).lower()
        name_extra = str(secrets.randbelow(99))
        return self.email_generator(first_name, last_name, name_extra, domain)
        

    def email_generator(self, first_name, last_name, name_extra, domain):
        """Return a random email address
        
        Keyword arguments:

        first_name STRING   First name
        last_name STRING    Last name
        name_extra STRING   Number
        domain STRING       Domain name
        """
        email_option = secrets.randbelow(27)
        if email_option == 0:
            return f"{first_name}{last_name}{name_extra}@{domain}"
        elif email_option == 1:
            return f"{first_name[:1]}{last_name}{name_extra}@{domain}"
        elif email_option == 2:
            return f"{first_name}{last_name[:1]}{name_extra}@{domain}"
        elif email_option == 3:
            return f"{last_name[:1]}{first_name}{name_extra}@{domain}"
        elif email_option == 4:
            return f"{last_name}{first_name[:1]}{name_extra}@{domain}"
        elif email_option == 5:
            return f"{last_name}{first_name}{name_extra}@{domain}"
        elif email_option == 6:
            return f"{first_name}{name_extra}@{domain}"
        elif email_option == 7:
            return f"{last_name}{name_extra}@{domain}"
        elif email_option == 8:
            return f"{first_name}{last_name}@{domain}"
        elif email_option == 9:
            return f"{first_name[:1]}{last_name}@{domain}"
        elif email_option == 10:
            return f"{first_name}{last_name[:1]}@{domain}"
        elif email_option == 11:
            return f"{last_name[:1]}{first_name}@{domain}"
        elif email_option == 12:
            return f"{last_name}{first_name[:1]}@{domain}"
        elif email_option == 13:
            return f"{last_name}{first_name}@{domain}"
        elif email_option == 14:
            return f"{first_name}@{domain}"
        elif email_option == 15:
            return f"{last_name}@{domain}"
        elif email_option == 16:
            return f"{first_name}.{last_name}{name_extra}@{domain}"
        elif email_option == 17:
            return f"{first_name[:1]}.{last_name}{name_extra}@{domain}"
        elif email_option == 18:
            return f"{first_name}.{last_name[:1]}{name_extra}@{domain}"
        elif email_option == 19:
            return f"{last_name[:1]}.{first_name}{name_extra}@{domain}"
        elif email_option == 20:
            return f"{last_name}.{first_name[:1]}{name_extra}@{domain}"
        elif email_option == 21:
            return f"{last_name}.{first_name}{name_extra}@{domain}"
        elif email_option == 22:
            return f"{first_name}.{last_name}@{domain}"
        elif email_option == 23:
            return f"{first_name[:1]}.{last_name}@{domain}"
        elif email_option == 24:
            return f"{first_name}.{last_name[:1]}@{domain}"
        elif email_option == 25:
            return f"{last_name[:1]}.{first_name}@{domain}"
        elif email_option == 26:
            return f"{last_name}.{first_name[:1]}@{domain}"
        elif email_option == 27:
            return f"{last_name}.{first_name}@{domain}"
    

    def password(self, min, max):
        """Return a cryptographically random password

        min INTEGER     Minimum password length
        max INTEGER     Maximum password length
        """
        password_length = secrets.randbelow(max-min) + min
        return "".join(secrets.choice(self.chars) for i in range(password_length))


    def headers(self):
        return {
            'User-Agent': self.ua.random,
        }
