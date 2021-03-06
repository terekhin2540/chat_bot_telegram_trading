from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters, CommandHandler
from typing import List


class Bot:
    def __init__(self, token: str):
        self.updater = Updater(token=token, use_context=True)
        self.dispatcher = self.updater.dispatcher
        self.descriptions = []

    def run(self):
        self.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), self.start_command))
        self.dispatcher.add_handler(CommandHandler('start', self.start_command))
        print('Bot started...Lets go!')
        self.updater.start_polling()

    def start_command(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text='Введи команду!!')
        # for description in self.descriptions:
        #     context.bot.send_message(chat_id=update.effective_chat.id, text=f'{description} \n')

    def register(self, module, query: List[str], description: str = 'Описание модуля', module_type: str = 'message'):
        if module_type == 'message':
            self.dispatcher.add_handler(MessageHandler(Filters.text(query), module.run))
        else:
            self.dispatcher.add_handler(MessageHandler(Filters.photo, module.run))
        self.descriptions.append(description)

