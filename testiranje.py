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


bank_accounts = [
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
    'bank_account': bank_accounts
}

MIN_DEPOSIT = 100.00


def display_account_details(accounts:list):
    for account in accounts:
        for key, value in account.items():
            if type(value) == dict:
                print(f'\n{key.upper()}')
                for sub_key, sub_value in value.items():
                    if type(sub_value) == dict:
                        print(f'    {sub_key.upper()}')
                        for sub_sub_key, sub_sub_value in sub_value.items():
                            print(f"        {sub_sub_key.upper()}: {sub_sub_value}")
                    else:
                      print(f'{sub_key}: {sub_value}')
            else:
                print(f"{key}: {value}")

# display_account_details(bank_accounts)


def create_bank_account():
    while True:
        try:
            deposit = float(input(f'Unesite iznos, minimalni iznos je {MIN_DEPOSIT} {currency["code"]}: '))
        except ValueError:
            print('Neispravan unos, pokusajte ponovno. ')
            continue

        if deposit < MIN_DEPOSIT:
             print(f'Iznos nije dovoljan, minimalni deposit je {MIN_DEPOSIT}')
        else:
            break

    today = datetime.now().strftime('$A %d.%m.%Y')
    new_id = bank_accounts[-1]['id'] + 1


    account = {}
    account['id'] = new_id
    account['iban'] = input('Unesite IBAN ')
    account['balance']= deposit
    account['opening_date']= today
    account['bank'] = bank
    account['currency'] = currency
    account['transactions'] = transactions

    bank_accounts.append(account)
    
    next_account = input('Zelite li unijeti novi kontakt? (Da/Ne): ')
    if next_account.lower() != 'da':
        return

    return account
        


create_bank_account()