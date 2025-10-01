#region INIT DATA

bank = {
    'id': 1,
    'name': 'Lipa po lipa d.d.',
    'hq': {
        'street': 'Kratka ulica 5',
        'postal_code': '10290',
        'city': 'Zapresic',
        'country': 'Hrvatska'
    }
}


currency = {
    'id': 1,
    'name': 'Euro',
    'symbol': '€',
    'code': 'EUR'
}


transactions = []
'''
id; date_time; amount; currency; bank_account; transaction_type [withdraw, deposit]
'''


bank_account = {
    'id': 1,
    'IBAN': 'HR45875465481354654',
    'balance': 0.00,
    'opening_date': '2025-09-29',
    'bank': bank,
    'currency': currency,
    'transactions': transactions
}


company = {
    'id': 1,
    'name': 'ABC Software d.o.o.',
    'tax_id': '01234567890',
    'hq': {
        'street': 'Duga ulica 15',
        'postal_code': '10290',
        'city': 'Zapresic',
        'country': 'Hrvatska'
    },
    'email': 'info@abc-software.hr',
    'bank_account': bank_account
}

#endregion
def transform_key(key: str) -> None:
    keys = key.split('_')
    if len(keys) == 1:
        return keys[0].capitalize() 
    else:
        text = ''
        for index, element in enumerate(keys):
            if index == 0:
                text += f'{element.capitalize()} '
            elif index == len(keys) - 1:
                text += f'{element} '
            else:
                text += f'{element} '
        return text


def print_dict(dictionary: dict = {}) -> None:
    if dictionary != {}:
        for key, value in dictionary.items():
            key = transform_key(key)

            if type(value) == dict:
                print()
                print(key)
                print_dict(value)
            else:   
                row = f'{key:<15} {str(value):<25}'
                print(row)

    else:
        print('Rijecnik nema niti jedan element. ')


print_dict(company)
