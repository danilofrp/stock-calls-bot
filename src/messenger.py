import telegram

class TelegramBot():
    def __init__(self, token, chat_ids):
        self.__chat_ids = chat_ids
        
        self.__bot = telegram.Bot(token = token)
        
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