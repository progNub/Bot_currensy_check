from databases import read_query, write_to_db

BYN = 'byn'
USD = 'usd'
RUB = 'rub'
EUR = 'eur'


class Money:

    def __init__(self, count=0):
        self.count = count

    @staticmethod
    def _create_table_money(str_name_table):
        create_table_database = f"""CREATE TABLE {str_name_table} (
              id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
              user_id int not null,
              count FLOAT,
              CONSTRAINT byn_users_id_user_id_telegram
                FOREIGN KEY (user_id) REFERENCES user (id_telegram)
                ON DELETE CASCADE);"""
        return write_to_db(create_table_database)

    @staticmethod
    def _drop_table_money(str_name_table):
        sql_del = f"drop table {str_name_table};"
        return write_to_db(sql_del)

    @staticmethod
    def _add_money(user_id, money, str_name_table):
        sql = f"""INSERT INTO
            {str_name_table} ( 
            user_id, count)
            VALUES (
            {user_id},{money});"""
        return write_to_db(sql)

    @staticmethod
    def _get_last_record(user_id, str_name_table):
        sql = f"""select count from {str_name_table} where user_id = {user_id} ORDER BY ID DESC LIMIT 1;"""
        return read_query(sql)


class Byn(Money):

    @staticmethod
    def create_table_money():
        return Money._create_table_money(BYN)

    @staticmethod
    def drop_table_money():
        return Money._drop_table_money(BYN)

    @staticmethod
    def add_money(user_id, money):
        return Money._add_money(user_id, money, BYN)

    @staticmethod
    def get_last_record(user_id):
        return Money._get_last_record(user_id, BYN)


class Usd(Money):
    @staticmethod
    def create_table_money():
        return Money._create_table_money(USD)

    @staticmethod
    def drop_table_money():
        return Money._drop_table_money(USD)

    @staticmethod
    def add_money(user_id, money):
        return Money._add_money(user_id, money, USD)

    @staticmethod
    def get_last_record(user_id):
        return Money._get_last_record(user_id, USD)


class Rub(Money):
    @staticmethod
    def create_table_money():
        return Money._create_table_money(RUB)

    @staticmethod
    def drop_table_money():
        return Money._drop_table_money(RUB)

    @staticmethod
    def add_money(user_id, money):
        return Money._add_money(user_id, money, RUB)

    @staticmethod
    def get_last_record(user_id):
        return Money._get_last_record(user_id, RUB)


class Eur(Money):
    @staticmethod
    def create_table_money():
        return Money._create_table_money(EUR)

    @staticmethod
    def drop_table_money():
        return Money._drop_table_money(EUR)

    @staticmethod
    def add_money(user_id, money):
        return Money._add_money(user_id, money, EUR)

    @staticmethod
    def get_last_record(user_id):
        return Money._get_last_record(user_id, EUR)

def drop_all_currency():
    Rub.drop_table_money()
    Byn.drop_table_money()
    Eur.drop_table_money()
    Usd.drop_table_money()


def create_all_currency():
    Rub.create_table_money()
    Byn.create_table_money()
    Eur.create_table_money()
    Usd.create_table_money()
