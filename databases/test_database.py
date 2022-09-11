from databases import Database


def get_all_writes_from_database():
    user = Database.read_query("select * from user")
    curs = Database.read_query("select * from curs")
    byn = Database.read_query("select * from byn")
    usd = Database.read_query("select * from usd")
    eur = Database.read_query("select * from eur")
    rub = Database.read_query("select * from rub")

    print("Содержимое базы данных:\n")
    print('user : ' + 'всего записей ' + str(len(user)) + '\n' + str(user))
    print('curs : ' + 'всего записей ' + str(len(curs)) + '\n' + str(curs))
    print('byn : ' + 'всего записей ' + str(len(byn)) + '\n' + str(byn))
    print('eur : ' + 'всего записей ' + str(len(eur)) + '\n' + str(eur))
    print('rub : ' + 'всего записей ' + str(len(rub)) + '\n' + str(rub))
    print('usd : ' + 'всего записей ' + str(len(usd)) + '\n' + str(usd))


get_all_writes_from_database()
