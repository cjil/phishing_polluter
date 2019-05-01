import os
import secrets
import string
import json


class Account():
    """Account

    Variables:
        first_name
        last_name
        domain
        chars
    Methods:
        get_first_name()
        get_last_name()
        get_domain()
        get_name_extra()
        get_email_option()
        get_email_address()
        set_password(min_length, max_length)
        get_password()
        set_random_option(list_of_options)
        set_email_option()
        set_name_extra()

    """

    def __init__(self, 
        first_names=None, last_names=None, domains=None, 
        min_length=None, max_length=None, email_option=None):
        """Initialise the class

        Keyword arguments:

        first_names LIST    First names
        last_names LIST     Last names
        domains LIST        Domain names
        """
        if first_names == None:
            with open('first_names.json') as f:
                first_names = json.loads(f.read())
        if last_names == None:
            with open('last_names.json') as f:
                last_names = json.loads(f.read())
        if domains == None:
            with open('domains.json') as f:
                domains = json.loads(f.read())
        min_length = 8 if min_length == None else min_length
        max_length = min_length + 4 if max_length == None else max_length
        self.email_option = self.set_email_option() if email_option == None else email_option
        self.first_name = self.set_random_option(
            list_of_options=[first_name.lower() for first_name in first_names])
        self.last_name = self.set_random_option(
            list_of_options=[last_name.lower() for last_name in last_names])
        self.domain = self.set_random_option(
            list_of_options=[domain.lower() for domain in domains])
        self.chars = f'{string.ascii_letters}{string.digits}!@#$%^&*()'
        self.name_extra = self.set_name_extra()
        self.password = self.set_password(
            min_length=min_length,
            max_length=max_length)
        self.email_address = self.set_email_address()
        

    def set_random_option(self, list_of_options):
        return secrets.SystemRandom().choice(list_of_options)

    
    def set_email_option(self):
        return secrets.randbelow(27)


    def set_name_extra(self):
        return str(secrets.randbelow(99))


    def get_first_name(self):
        """Return a random first name
        """
        return self.first_name

    
    def get_last_name(self):
        """Return a random last name
        """
        return self.last_name
    

    def get_domain(self):
        """Return a random domain name
        """
        return self.domain


    def get_name_extra(self):
        """Return a random number
        """
        return self.name_extra


    def get_email_option(self):
        """Return a random number between 0 and 27
        """
        return self.email_option


    def set_email_address(self, email_option=None):
        """Return a random email address

        Keyword arguments:

        first_name STRING   First name
        last_name STRING    Last name
        name_extra STRING   Number
        domain STRING       Domain name
        email_option INT    Email address type to select
        """
        email_option = self.email_option if email_option == None else email_option
        if email_option == 0:
            return f"{self.first_name}{self.last_name}{self.name_extra}@{self.domain}"
        elif email_option == 1:
            return f"{self.first_name[:1]}{self.last_name}{self.name_extra}@{self.domain}"
        elif email_option == 2:
            return f"{self.first_name}{self.last_name[:1]}{self.name_extra}@{self.domain}"
        elif email_option == 3:
            return f"{self.last_name[:1]}{self.first_name}{self.name_extra}@{self.domain}"
        elif email_option == 4:
            return f"{self.last_name}{self.first_name[:1]}{self.name_extra}@{self.domain}"
        elif email_option == 5:
            return f"{self.last_name}{self.first_name}{self.name_extra}@{self.domain}"
        elif email_option == 6:
            return f"{self.first_name}{self.name_extra}@{self.domain}"
        elif email_option == 7:
            return f"{self.last_name}{self.name_extra}@{self.domain}"
        elif email_option == 8:
            return f"{self.first_name}{self.last_name}@{self.domain}"
        elif email_option == 9:
            return f"{self.first_name[:1]}{self.last_name}@{self.domain}"
        elif email_option == 10:
            return f"{self.first_name}{self.last_name[:1]}@{self.domain}"
        elif email_option == 11:
            return f"{self.last_name[:1]}{self.first_name}@{self.domain}"
        elif email_option == 12:
            return f"{self.last_name}{self.first_name[:1]}@{self.domain}"
        elif email_option == 13:
            return f"{self.last_name}{self.first_name}@{self.domain}"
        elif email_option == 14:
            return f"{self.first_name}@{self.domain}"
        elif email_option == 15:
            return f"{self.last_name}@{self.domain}"
        elif email_option == 16:
            return f"{self.first_name}.{self.last_name}{self.name_extra}@{self.domain}"
        elif email_option == 17:
            return f"{self.first_name[:1]}.{self.last_name}{self.name_extra}@{self.domain}"
        elif email_option == 18:
            return f"{self.first_name}.{self.last_name[:1]}{self.name_extra}@{self.domain}"
        elif email_option == 19:
            return f"{self.last_name[:1]}.{self.first_name}{self.name_extra}@{self.domain}"
        elif email_option == 20:
            return f"{self.last_name}.{self.first_name[:1]}{self.name_extra}@{self.domain}"
        elif email_option == 21:
            return f"{self.last_name}.{self.first_name}{self.name_extra}@{self.domain}"
        elif email_option == 22:
            return f"{self.first_name}.{self.last_name}@{self.domain}"
        elif email_option == 23:
            return f"{self.first_name[:1]}.{self.last_name}@{self.domain}"
        elif email_option == 24:
            return f"{self.first_name}.{self.last_name[:1]}@{self.domain}"
        elif email_option == 25:
            return f"{self.last_name[:1]}.{self.first_name}@{self.domain}"
        elif email_option == 26:
            return f"{self.last_name}.{self.first_name[:1]}@{self.domain}"
        elif email_option == 27:
            return f"{self.last_name}.{self.first_name}@{self.domain}"
        elif email_option > 27:
            raise ValueError(f'Email option selected does not exist')


    def get_email_address(self):
        return self.email_address


    def set_password(self, min_length, max_length):
        """Return a cryptographically random password

        min INTEGER     Minimum password length
        max INTEGER     Maximum password length
        """
        if min_length > max_length:
            raise ValueError(f'Minimum value ({min_length}) should be less than maximum value ({max_length})')
        password_length = secrets.randbelow(max_length-min_length) + min_length
        return "".join(
            secrets.choice(self.chars) for i in range(password_length))
    
    def get_password(self):
        return self.password

