import os
import re
import log
import utils
import requests
from errors import LoginError
from datetime import datetime
from bs4 import BeautifulSoup

datetime_regex = re.compile(r'\d{2}/\d{2}/\d{4} \d{1,2}:\d{2}')

base_url = 'https://grandetacada.com.br'
login_url = 'https://grandetacada.com.br/login'
login_credencials_file = os.path.join('.', 'credentials', '') + 'login_credentials.json'
login_credentials = utils.read_json(login_credencials_file)

last_call_file = os.path.join('.', 'log', '') + 'last_sent_call.json'


def get_calls():
    token, cookies = get_token_and_cookies()
    response = login_to_call_history(token, cookies)
    
    soup = BeautifulSoup(response.text)
    cards = soup.find_all('div', attrs = {'class': 'card'})
    calls = list(map(card_to_dict, cards))
    return calls


def get_token_and_cookies():
    response = requests.get(url = base_url)
    data = response.text
    soup = BeautifulSoup(data)
    hidden_input_tag = soup.find('input', attrs = {'name': '_token'})
    token = hidden_input_tag.get('value')
    cookies = response.cookies
    return token, cookies


def login_to_call_history(_token, cookies):
    login_data = {
        '_token': _token,
        'email': login_credentials['email'],
        'password': login_credentials['password']
    }
    response = requests.post(url = login_url, data = login_data, cookies = cookies)
    if response.status_code != 200:
        raise LoginError(f'Login error: status code {response.status_code}')
        
    return response


def card_to_dict(card):
    card_text = card.find('p').text
    card_datetime_text = card.find('em').text
    call_datetime = get_call_datetime(card_datetime_text)
    datetime_str = call_datetime.strftime("%Y-%m-%d %H:%M")

    call = {
        'source': 'A Grande Tacada',
        'datetime': call_datetime,
        'text': card_text,
        'message': f'{card_text}\n\n_(sent in {datetime_str})_'
    }
    return call


def get_call_datetime(card_datetime_text):
    datetime_match = datetime_regex.search(card_datetime_text)
    datetime_str = datetime_match.group(0)
    call_datetime = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M')
    return call_datetime