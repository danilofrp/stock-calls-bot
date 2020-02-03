import os
import re
import log
import utils
import scrapper
import requests
import messenger
from errors import LoginError
from datetime import datetime
from bs4 import BeautifulSoup

base_path = os.path.split(os.path.realpath(__file__))[0]

last_call_file = os.path.join(base_path, 'log', '') + 'last_sent_call.json'

bot_config_file = os.path.join(base_path, 'bot_specs', '') + 'bot_config.json'
bot_config = utils.read_json(bot_config_file)

def main():
    try:
        logger = log.get_logger(name = 'scrapper')
        messenger_bot = messenger.TelegramBot(**bot_config)
        
        try:
            calls = scrapper.get_calls()
        except LoginError as e:
            logger.error(e)
            return

        calls_to_send = define_calls_to_send(calls)
        for call in calls_to_send:
            messenger_bot.send_message(call['message'])
            save_last_call_sent(call)
    except Exception as e:
            logger.error(e)
            return


def define_calls_to_send(calls):
    last_call = get_last_call_sent()
    call_filter = lambda c: c['datetime'] >= last_call['datetime'] and c['text'] != last_call['text']
    calls_to_send = list(filter(call_filter, calls))
    calls_to_send = list(reversed(calls_to_send))

    return calls_to_send


def get_last_call_sent():
    if os.path.isfile(last_call_file):
        last_call = utils.read_json(last_call_file)
        last_call['datetime'] = datetime.strptime(last_call['datetime'], "%Y-%m-%d %H:%M")
        return last_call
    else:
        return {
            'source': 'mock',
            'datetime': datetime(1900, 1, 1),
            'text': 'mock_call',
            'message': 'mock_call_message',
        }


def save_last_call_sent(call):
    call['datetime'] = call['datetime'].strftime("%Y-%m-%d %H:%M")
    utils.write_json(last_call_file, call)



if __name__ == "__main__":
    main()