import os
import secrets
import string
import json


class Accounts():
    """Accounts

    Variables:
        first_names
        last_names
        domains
        chars
    Methods:
        get_first_name()
        get_last_name()
        get_domain()
        get_name_extra()
        get_email_option()
        email_generator(first_name, last_name, name_extra, domain, email_option)
        password(min, max)
    """

    def __init__(self, first_names=None, last_names=None, domains=None):
        """Initialise the class

        Keyword arguments:

        first_names LIST    First names
        last_names LIST     Last names
        domains LIST        Domain names
        """
        if first_names == None:
            first_names = json.loads(open('first_names.json').read())
        if last_names == None:
            last_names = json.loads(open('last_names.json').read())
        if domains == None:
            domains = json.loads(open('domains.json').read())
        self.first_names = [first_name.lower() for first_name in first_names]
        self.last_names = [last_name.lower() for last_name in last_names]
        self.domains = [domain.lower() for domain in domains]
        self.chars = f'{string.ascii_letters}{string.digits}!@#$%^&*()'
        self.random_choice = secrets.SystemRandom().choice

    def get_first_name(self):
        """Return a random first name
        """
        return self.random_choice(self.first_names)
    
    def get_last_name(self):
        """Return a random last name
        """
        return self.random_choice(self.last_names)
    
    def get_domain(self):
        """Return a random domain name
        """
        return self.random_choice(self.domains)

    def get_name_extra(self):
        """Return a random number
        """
        return str(secrets.randbelow(99))

    def get_email_option(self):
        """Return a random number between 0 and 27
        """
        return secrets.randbelow(27)

    def email_generator(self, first_name, last_name, name_extra, domain, email_option):
        """Return a random email address

        Keyword arguments:

        first_name STRING   First name
        last_name STRING    Last name
        name_extra STRING   Number
        domain STRING       Domain name
        email_option INT    Email address type to select
        """
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
        elif email_option > 27:
            raise ValueError(f'Email option selected does not exist')

    def password(self, _min, _max):
        """Return a cryptographically random password

        min INTEGER     Minimum password length
        max INTEGER     Maximum password length
        """
        if _min > _max:
            raise ValueError(f'Minimum value ({_min}) should be less than maximum value ({_max})')
        password_length = secrets.randbelow(_max-_min) + _min
        return "".join(
            secrets.choice(self.chars) for i in range(password_length))

