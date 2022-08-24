from databases import read_query, write_to_db


class Usd(object):
    def __init__(self, count=0):
        self.count = count

    @staticmethod
    def create_table_money():
        create_table_database = """CREATE TABLE usd (
          id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
          user_id int not null,
          count FLOAT,
          CONSTRAINT usd_users_id_user_id_telegram
            FOREIGN KEY (user_id) REFERENCES user (id_telegram)
            ON DELETE CASCADE);"""
        write_to_db(create_table_database)

    @staticmethod
    def drop_table_money():
        sql_del = "drop table usd;"
        write_to_db(sql_del)

    @staticmethod
    def add_money(user_id, money):
        sql = f"""INSERT INTO
        usd ( 
        user_id, count)
        VALUES (
        {user_id},{money});"""
        write_to_db(sql)


class Rub(object):
    def __init__(self, count=0):
        self.count = count

    @staticmethod
    def create_table_money():
        create_table_database = """CREATE TABLE rub (
          id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
          user_id int not null,
          count FLOAT,
          CONSTRAINT rub_users_id_user_id_telegram
            FOREIGN KEY (user_id) REFERENCES user (id_telegram)
            ON DELETE CASCADE);"""
        write_to_db(create_table_database)

    @staticmethod
    def drop_table_money():
        sql_del = "drop table rub;"
        write_to_db(sql_del)

    @staticmethod
    def add_money(user_id, money):
        sql = f"""INSERT INTO
        rub ( 
        user_id, count)
        VALUES (
        {user_id},{money});"""
        write_to_db(sql)


class Eur(object):
    def __init__(self, count=0):
        self.count = count

    @staticmethod
    def create_table_money():
        create_table_database = """CREATE TABLE eur (
          id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
          user_id int not null,
          count FLOAT,
          CONSTRAINT eur_users_id_user_id_telegram
            FOREIGN KEY (user_id) REFERENCES user (id_telegram)
            ON DELETE CASCADE);"""
        write_to_db(create_table_database)

    @staticmethod
    def drop_table_money():
        sql_del = "drop table eur;"
        write_to_db(sql_del)

    @staticmethod
    def add_money(user_id, money):
        sql = f"""INSERT INTO
        eur ( 
        user_id, count)
        VALUES (
        {user_id},{money});"""
        write_to_db(sql)


class Byn(object):
    def __init__(self, count=0):
        self.count = count

    @staticmethod
    def create_table_money():
        create_table_database = """CREATE TABLE byn (
          id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
          user_id int not null,
          count FLOAT,
          CONSTRAINT byn_users_id_user_id_telegram
            FOREIGN KEY (user_id) REFERENCES user (id_telegram)
            ON DELETE CASCADE);"""
        write_to_db(create_table_database)

    @staticmethod
    def drop_table_money():
        sql_del = "drop table byn;"
        write_to_db(sql_del)

    @staticmethod
    def add_money(user_id, money):
        sql = f"""INSERT INTO
        byn ( 
        user_id, count)
        VALUES (
        {user_id},{money});"""
        write_to_db(sql)


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
