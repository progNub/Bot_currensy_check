from databases import read_query, write_to_db
from for_requests import nbrb


class Curs(object):
    def __init__(self, RUB=0, USD=0, EUR=0):
        """rub, usd, eur"""
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
        return write_to_db(create_table_database)

    @staticmethod
    def drop_table_curs():
        sql_del = "drop table curs;"
        return write_to_db(sql_del)

    @staticmethod
    def add_curs(curs):
        sql = f"""INSERT INTO
        curs ( 
        rub, usd, eur)
        VALUES (
        {curs.RUB}, {curs.USD}, {curs.EUR});"""
        return write_to_db(sql)

    @staticmethod
    def update_all_curs_today():
        rub = nbrb.get_rate_rub()
        eur = nbrb.get_rate_eur()
        usd = nbrb.get_rate_usd()
        curs = Curs(RUB=rub, USD=usd, EUR=eur)
        Curs.update_curs(curs)

    @staticmethod
    def update_curs(curs):
        sql = f"delete from curs where id >= 1;"
        write_to_db(sql)
        sql = f"""INSERT INTO
                curs ( 
                rub, usd, eur)
                VALUES (
                {curs.RUB}, {curs.USD}, {curs.EUR});"""
        return write_to_db(sql)

    @staticmethod
    def get_last_all_curs():
        sql = """SELECT * FROM curs ORDER BY ID DESC LIMIT 1"""
        return read_query(sql)

    @staticmethod
    def get_last_curs_eur():
        sql = """SELECT eur FROM curs ORDER BY ID DESC LIMIT 1"""
        return read_query(sql)

    @staticmethod
    def get_last_curs_usd():
        sql = """SELECT usd FROM curs ORDER BY ID DESC LIMIT 1"""
        return read_query(sql)

    @staticmethod
    def get_last_curs_rub():
        sql = """SELECT rub FROM curs ORDER BY ID DESC LIMIT 1"""
        return read_query(sql)
