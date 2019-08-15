import os
import utils
import telegram

class TelegramBot():
    def __init__(self):
        bot_config_file = os.path.join('.', 'bot_specs', '') + 'bot_config.json'
        bot_config = utils.read_json(bot_config_file)
            
        self.__bot_token = bot_config['token']
        self.__chat_ids = bot_config['chat_ids']
        
        self.__bot = telegram.Bot(token = self.__bot_token)
        
    def send_message(self, message, chat_id = None):
        if chat_id:
            self.__bot.sendMessage(chat_id, text = message, parse_mode  = 'markdown')
        else:
            for chat_id in self.__chat_ids:
                self.__bot.sendMessage(chat_id, text = message, parse_mode  = 'markdown')

    def send_messages(self, messages):
        for chat_id in self.__chat_ids:
            for message in messages:
                self.send_message(message, chat_id)