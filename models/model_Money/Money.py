from databases import Database


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
        return Database.write_to_db(create_table_database)

    @staticmethod
    def _drop_table_money(str_name_table):
        sql_del = f"drop table {str_name_table};"
        return Database.write_to_db(sql_del)

    @staticmethod
    def _add_money(user_id, money, str_name_table):
        sql = f"""INSERT INTO
            {str_name_table} ( 
            user_id, count)
            VALUES (
            {user_id},{money});"""
        return Database.write_to_db(sql)

    @staticmethod
    def _get_last_record(user_id, str_name_table):
        sql = f"""select count from {str_name_table} where user_id = {user_id} ORDER BY ID DESC LIMIT 1;"""
        return Database.read_query(sql)
