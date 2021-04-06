from sql_vars import queries
from sql_tool import Database as SQL


class User:
    def __init__(self, user_id, user_fname):
        self.id = user_id
        self.language = None
        self.first_name = user_fname

    def create(self):
        """
        Create user: add user to users table, save his id and preferences
        :return: dict
        """
        print(f'[EVENT] Creating new user. ID: {self.id}')
        query = queries['users']['check_id'].format(user_id=self.id)
        result = SQL(query).get()
        if len(result) == 0:
            query = queries['users']['create'].format(user_id=self.id, firstname=self.first_name)
            SQL(query).run()
            print(f'--- user {self.id} now in database')
        else:
            print(f"[WARNING] user {self.id} already exists.")

    def set_lang(self):
        """
        Set users language and save to db
        :return: dict
        """
        # check users table, select users current language, update language

    def set_first_name(self):
        """
        Save user's language settings
        :return: dict
        """
        # check users table, select users current firstname, update firstname


"""
    1. Класс юзер, у него есть методы для настроек всех атрибутов юзера
    2. Класс ивентов, чтобы отслеживать добавление метрики
    3. Определить полную логику работы бд
"""