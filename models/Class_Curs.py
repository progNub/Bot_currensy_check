from databases import read_query, write_to_db


class Curs(object):
    def __init__(self, RUB=0, USD=0, EUR=0):
        self.RUB = RUB
        self.USD = USD
        self.EUR = EUR

    @staticmethod
    def create_table_curs():
        create_table_database = """CREATE TABLE curs (
          id INT PRIMARY KEY AUTO_INCREMENT PRIMARY KEY,
          rub FLOAT,
          usd FLOAT,
          eur FLOAT);"""
        write_to_db(create_table_database)

    @staticmethod
    def drop_table_curs():
        sql_del = "drop table curs;"
        write_to_db(sql_del)

    @staticmethod
    def add_curs(curs):
        sql = f"""INSERT INTO
        curs ( 
        rub, usd, eur)
        VALUES (
        {curs.RUB}, {curs.USD}, {curs.EUR});"""
        write_to_db(sql)


