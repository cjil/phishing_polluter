# phishing_polluter
Pollute phishing attempts with fake username/password combinations

Based on the youtube video of Engineer Man, I expanded upon it as an exercise to provide more pollution to the phishing scammers files in a shorter time.

## Improvments
1. asyncio to add more username/passwords per second than the original
2. added additional domain names to use
3. using first and last name lists to generate a larger variety of email addresses
4. created rules for firstname / lastname combinations (e.g. first initial + last name, last name + first initial, first name + last name, etc)

## Installation
Clone the git repository
pip install -r requirements.txt

## Usage
python phishing_polluter --help
python phishing_polluter <TARGET_URL> [--username_code] [--password_code]

## Options
### qty
* Number of email address / password combinations to pollute the list with
### username_code
* Username POST field name
### password_code
* Password POST field name
