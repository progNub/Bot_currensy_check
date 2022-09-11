from models.model_Money import Money


class Rub(Money):
    current_money = 'rub'

    @staticmethod
    def create_table_money():
        return Money._create_table_money(Rub.current_money)

    @staticmethod
    def drop_table_money():
        return Money._drop_table_money(Rub.current_money)

    @staticmethod
    def add_money(user_id, money):
        return Money._add_money(user_id, money, Rub.current_money)

    @staticmethod
    def get_last_record(user_id):
        result = Money._get_last_record(user_id, Rub.current_money)
        if len(result) == 0:
            return 0
        else:
            return result[0][0]
