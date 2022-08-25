from databases import read_query

sql = "select * from user"
user = read_query(sql)
sql = "select * from curs"
curs = read_query(sql)
sql = "select * from byn"
byn = read_query(sql)
sql = "select * from usd"
usd = read_query(sql)
sql = "select * from eur"
eur = read_query(sql)
sql = "select * from rub"
rub = read_query(sql)
print("Содержимое базы данных:\n")
print('user : '+str(user))
print('curs : '+str(curs))
print('byn : '+str(byn))
print('eur : '+str(eur))
print('rub : '+str(rub))
print('usd : '+str(usd))



