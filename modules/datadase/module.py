from modules.base_module import BaseModule
import telegram.bot, telegram, sqlite3
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import sqlite3


class Add_to_db(BaseModule):
    def run(self, update, context):
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS login_id_new(
        id INTEGER
        )""")
        connect.commit()

        people_id = update.effective_chat.id
        cursor.execute(f"SELECT id FROM login_id_new WHERE id == {people_id}")
        data = cursor.fetchone()
        if data is None:
            user_id = [update.effective_chat.id]
            cursor.execute("INSERT INTO login_id_new VALUES(?);", user_id)
            connect.commit()
            self.send(update, context, text="Ты был зарегистрирован!!!")
        else:
            self.send(update, context, text="Такой пользователь уже зарегистрирован!!!")


class DELETE_from_db(BaseModule):
    def run(self, update, context):
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()

        id_for_delete = update.effective_chat.id
        print(id_for_delete)
        cursor.execute(f"DELETE FROM login_id_new WHERE id == {id_for_delete}")
        connect.commit()
        self.send(update, context, text="Пользователь был удален!")
        # data = cursor.fetchone()
        # if data is None:
        #     self.send(update, context, text="Такого пользователя нет в базе данных")
        # else:
        #     cursor.execute(f"DELETE id FROM login_id_new WHERE id == {people_id}")
        #     connect.commit()
        #     self.send(update, context, text="Пользователь был удален!")


add_to_bd_module = Add_to_db()
delete_from_bd_module = DELETE_from_db()
