import aiogram.types
from databases import Database


class UserManager(object):

    @staticmethod
    def create_database_table_users():
        create_table_database = """CREATE TABLE user
            (
                id INT AUTO_INCREMENT primary key not null,
                id_telegram int not null UNIQUE,
                is_bot bool,
                first_name char(255),
                last_name char(255),
                username char(255));"""
        return Database.write_to_db(create_table_database)

    @staticmethod
    def drop_table_user():
        sql_del = "drop table user;"
        return Database.write_to_db(sql_del)

    @staticmethod
    def add_new_user(user: aiogram.types.User):
        """Возвращает True если успешно добавил пользователя иначе False"""
        sql = f"""INSERT INTO
            user ( id_telegram,
            is_bot,
            first_name,
            last_name,
            username,
            subs)
            VALUES (
            {user.id},
            {user.is_bot},
            '{user.first_name}',
            '{user.last_name}',
            '{user.username}',
            {False});"""
        return Database.write_to_db(sql)

    @staticmethod
    def subscribe(user_id):
        sql = f"""select subs from user where id_telegram = {user_id}"""
        subs = not (bool(Database.read_query(sql)[0][0]))
        sql = f"""update user set subs = {subs} where id_telegram = {user_id}"""
        return Database.write_to_db(sql)

    @staticmethod
    def check_subscribe(user_id):
        """get True - subscriber or False - not subscriber"""
        sql = f"""select subs from user where id_telegram = {user_id}"""
        return bool(Database.read_query(sql)[0][0])

    @staticmethod
    def get_list_subscribers():
        sql = f"""select id_telegram from user where subs = 1"""
        return Database.read_query(sql)

    @staticmethod
    def check_unique(user_id):
        """Возвращает True если это уникальный пользователь """
        check = f"(select * from user where id_telegram = '{user_id}');"
        return not (bool(len(Database.read_query(check))))

    @staticmethod
    def delete_user(id_user):
        delete_user = f"""DELETE FROM users WHERE id_telegram = '{id_user}'; """
        return Database.write_to_db(delete_user)

    @staticmethod
    def get_users_by_key(key='*'):
        return Database.read_query(f"select {key} from user;")

    @staticmethod
    def get_users_from_db(key="*"):
        return UserManager.get_users_by_key(key)
