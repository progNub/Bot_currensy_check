import requests
import json
import datetime

file_name = "../databases/valuta.json"


def get_rate_for_id_date(id_rate="431", date=datetime.date.today()):
    """Returned type 'float'"""
    temp = '0000'
    try:
        webpage = requests.get(f"https://www.nbrb.by/api/exrates/rates/{id_rate}?ondate={date}")
        money = webpage.json()
        temp = money.get('Cur_OfficialRate')
    except:
        print(f'not answer from https://www.nbrb.by/api/exrates/rates/{id_rate}')
        return False
    return temp


def get_rate_usd(date=datetime.date.today()):
    return get_rate_for_id_date(date=date)


def get_rate_rub(date=datetime.date.today()):
    return get_rate_for_id_date('456', date)


def get_rate_eur(date=datetime.date.today()):
    return get_rate_for_id_date('451', date)

# def get_all_rates():
#     temp = "0000"
#     try:
#         webpage = requests.get("https://www.nbrb.by/api/exrates/currencies")
#         temp = webpage.json()
#     except:
#         print('not answer from https://www.nbrb.by/api/exrates/currencies')
#     return temp


# def write_to_json():
#    try:
#        with open(file_name, 'w+') as f:
#            json.dump(get_all_rates(), f, indent=2)
#            print("write complite")
#    except IOError:
#        print("write is not complete: " + file_name)
