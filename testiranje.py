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

# dohvat id broja


def get_id(entity: dict) -> int:
    return entity['id']

company_id = get_id(company)
bank_account_id = get_id(bank_account)

print(company_id)
print(bank_account_id)