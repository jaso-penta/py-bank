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

#endregion

def create_bank_account(bank_account: list) -> dict:
    if bank_account:
        new_id = bank_account[-1]['id'] +1
    else:
        new_id = 1
    
    iban = input('Unesi IBAN: ')
    balance = float(input('Unesi početni iznos: '))
    opening_date = input('Unesi datum otvaranja računa (YYYY-MM-DD): ') 

    new_account = {
        'id' : new_id,
        'IBAN' : iban,
        'balance' : balance,
        'openinga_date' : opening_date,
        'bank': bank,
        'currency': currency,
        'transactions': []

    }

    bank_account.append(new_account)

    return new_account


   
            
            
         
        
create_bank_account(bank_account)
print(bank_account)

                
                
       

    

   

  



