import requests
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
