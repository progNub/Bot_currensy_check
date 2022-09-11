from models import Curs
from models.model_User import UserManager
from models.model_Money import Eur, Usd, Byn, Rub


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


Curs.drop_table_curs()
drop_all_currency()
UserManager.drop_table_user()

Curs.create_table_curs()
UserManager.create_database_table_users()
create_all_currency()

# Проверка работоспособности бд
