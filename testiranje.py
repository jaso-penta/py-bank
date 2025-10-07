from datetime import datetime
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


bank_account = [
    {
    'id': 1,
    'IBAN': 'HR45875465481354654',
    'balance': 0.00,
    'opening_date': '2025-09-29',
    'bank': bank,
    'currency': currency,
    'transactions': transactions
    }
]

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




def print_dict(data, indent=0) -> None:
    """
    Rekurzivno ispisuje sadržaj rječnika ili liste rječnika s uvlakama.
    """
    space = "  " * indent  # određuje razinu uvlake
    
    if isinstance(data, list):
        if not data:
            print(space + "Prazna lista.")
            return
        for item in data:
            if isinstance(item, (dict, list)):
                print_dict(item, indent)
                print(space + "-" * 40)
            else:
                print(space + str(item))
    
    elif isinstance(data, dict):
        if not data:
            print(space + "Rječnik nema niti jedan element.")
            return
        for key, value in data.items():
            if isinstance(value, dict):
                print(f"{space}{key}:")
                print_dict(value, indent + 1)
            elif isinstance(value, list):
                print(f"{space}{key}:")
                print_dict(value, indent + 1)
            else:
                print(f"{space}{key:<15} {str(value):<25}")
    else:
        print(space + str(data))



print_dict(bank_account)
