import json
import time
import asyncio
import click
from accounts import Account
import aiohttp
from fake_useragent import UserAgent
import sys


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


async def post_email(url, username_code, password_code, email=None, password=None, headers=None):
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
            if email == None:
                account = Account()
                email = account.email_address()
            if password == None:
                account = Account() if None else account
                password = account.password()
            if headers == None:
                ua = UserAgent()
                headers = { 'User-Agent': ua.random }
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
    url, username_code, password_code, number_of_email_addresses = (
        kwargs['url'],
        kwargs['username_code'],
        kwargs['password_code'],
        kwargs['qty']
    )
    if sys.platform == 'win32':
        loop = asyncio.ProactorEventLoop()
    else:
        loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    tasks = (
        post_email(
            url=url,
            username_code=username_code,
            password_code=password_code
        ) for i in range(0, number_of_email_addresses))
    future = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(future)
    finish_time = time.time() - start_time
    print(f'  execution time: {finish_time:.2f}s')
