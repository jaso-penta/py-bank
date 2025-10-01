#region IMPORTS
import os

#endregion


#region INIT DATA
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
    'email': 'info@abc-software.hr'
}

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

#endregion


#region FUNCTIONS
def wait_for_user():
    input('Za nastavak pritisnite tipku ENTER! ')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def logout_screen():
    print('Pozdrav')






def main():
    pass


#endregion


#region MAIN PROGRAM
if __name__ == '__main__':
    # ucitavanje pocetnih vrijednosti iz datoteka load_init_data()
    main()


#endregion


#region END PROGRAM
clear_screen()
logout_screen()
wait_for_user()
#endregion

