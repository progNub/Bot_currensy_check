from models import User, Curs
from models import Class_Money

Curs.drop_table_curs()
Class_Money.drop_all_currency()
User.drop_table_user()

Curs.create_table_curs()
User.create_database_table_users()
Class_Money.create_all_currency()

# Проверка работоспособности бд

# user = User(id=12345678)
# User.add_new_user(user)

# Class_Money.Byn.add_money(user.id, money=100)
# Class_Money.Eur.add_money(user.id, money=200)
# Class_Money.Usd.add_money(user.id, money=300)
# Class_Money.Rub.add_money(user.id, money=400)

# curs = Curs()
# Curs.add_curs(curs)
