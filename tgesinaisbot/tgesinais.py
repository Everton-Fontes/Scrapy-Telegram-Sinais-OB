import telebot
from config.config import TGE_SINAIS_ID, TGE_SINAIS_TOKEN


class Tge_Sinais:

    def __init__(self):
        self.bot = telebot.TeleBot(TGE_SINAIS_TOKEN)
        self.bot.config['api_key'] = TGE_SINAIS_TOKEN
        self.id = TGE_SINAIS_ID

    def send_message(self, message):
        return self.bot.send_message(self.id, message)


if __name__ == "__main__":
    pass
