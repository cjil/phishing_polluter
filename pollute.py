import json
import time
import asyncio
import click
from accounts import Accounts
import aiohttp


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


async def post_email(url, username_code, password_code, email, password, headers):
    """Send the username and password combination to the URL

    Keyword arguments:
    url TEXT            POST endpoint URL
    username_code TEXT  POST username identifier
    password_code TEXT  POST password identifier
    email TEXT          email address
    password TEXT       password
    """

    try:
        async with aiohttp.ClientSession() as session:
            print(f"Sending username: {email} and password {password}")
            await session.post(url, headers=headers, allow_redirects=False, data={
                username_code: email,
                password_code: password
            })
    except aiohttp.client_exceptions.ClientConnectionError:
        print(f"Unable to connect to {url}. {email} and password {password} unsuccessful.")
    except Exception as e:
        print(f"Error: {e}")


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(version='1.0.0')
@click.argument('url')
@click.option(
    '--qty',
    default=1000,
    help='Number of email/password combinations to generate')
@click.option(
    '--username_code',
    default='username',
    help='POST Username fieldname')
@click.option(
    '--password_code',
    default='password',
    help='POST Password fieldname')
def pollute(**kwargs):
    """Spam fake username & password combinations to the POST URL endpoint

    \b
    Keyword arguments:
    url TEXT            POST endpoint URL
    username_code TEXT  POST username identifier
    password_code TEXT  POST password identifier
    qty INTEGER         Number of email/password combinations to generate
    """
    start_time = time.time()

    url = kwargs['url']
    username_code = kwargs['username_code']
    password_code = kwargs['password_code']
    number_of_email_addresses = kwargs['qty']
    kwargs = None

    accounts = Accounts(
        json.loads(open('first_names.json').read()),
        json.loads(open('last_names.json').read()),
        json.loads(open('domains.json').read()))
    loop = asyncio.get_event_loop()
    tasks = [
        post_email(
            url,
            username_code,
            password_code,
            accounts.email(),
            accounts.password(8, 16),
            accounts.headers()
        ) for i in range(0, number_of_email_addresses)]
    future = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(future)
    finish_time = time.time() - start_time
    print(f'  execution time: {finish_time:.2f}s')
