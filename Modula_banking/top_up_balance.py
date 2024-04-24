from validator import validate_name
from validator import validate_iban

def topup_balance(name, surname, iban, money_amount, database):
    user = (name, surname)
    for user in database:
        if database[user]['iban'] == iban:
            database[user]['balance'] += money_amount
            return database
    return None
    
    
