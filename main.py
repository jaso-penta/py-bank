#region IMPORTS


#endregion


#region INIT DATA
import os
from posixpath import ismount
from datetime import datetime


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


bank_account = [
    {
    'id': 1,
    'account_number': '78799812',
    'iban': 'HR45875465481354654',
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


#region FUNCTIONS
def wait_for_user():
    input('Za nastavak pritisnite ENTER')


def clear_screen():
    os.system('clear')


def log_out_screen():
    print('Pozdrav')


def get_id(entity: dict) -> None:
    return entity['id']


def company_has_account():
    if company['bank_account'] == {}:
        return False
    else:
        return True


def display_account_details():
    pass


def key_transform(key: str) -> None:
    keys = key.split('_')
    if len(keys) == 1:
        return keys[0].capitalize()
    else:
        text = ''
        for index, element in enumerate(keys):
            if index == 0:
                text += f'{element.capitalize()} '
            elif index == len(keys) -1:
                text += f'{element} '
            else:
                text += f'{element} '
        return text


def print_dict(dictionary: dict = {}) -> None:
    if dictionary != {}:
        for key, value in dictionary.items():
            key = key_transform(key)
            
            if type(value) == dict:
                print()
                print(key)
                print_dict(value)
            else:
                row = f'{key:<15} {str(value):<25}'
                print(row)
    
    else:
        print('Rijecnik je prazan')


def get_valid_input(prompt: str, valid_options: list) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_options:
                return choice
            else:
                print(f'Netocan unos, odaberi jednu od opicja {valid_options}')
        except ValueError:
            print('Greska, morate unjeti broj')


def create_bank_account(bank_account: list) -> dict: 
    new_id = input('unesi id')
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



def main_menu():
    
    print()
    print(f'{"PYBANK":>25}')
    print('=' *50)
    print(f'{"MAIN MENU":>27}')
    print('=' *50)

    print('Izaberi opciju: ')
    print('1. Prikaz informacija racuna')
    print('2. Kreiraj novi racun')
    print('3. Informacije o racunu')
    print('4. Prikaz transakcija')
    print('5. Uplata sredstava')
    print('6. Isplata sredstava')
    print('7. Prikaz podataka o vlasniku racuna')
    print('0. EXIT')

    return get_valid_input('Upisite broj ispred akcije koju zelite pokrenuti: ', list(range(7)))


def main():
    if company_has_account():
        menu_item = main_menu()

        if menu_item == 0:
            return
        elif menu_item == 1:
            print_dict(bank_account)
            wait_for_user()
        elif menu_item == 2:
            create_bank_account(bank_account)
            wait_for_user

    else:
        print('Pokrenu funkciju za otvaranje racuna')
        create_bank_account(bank_account)
        wait_for_user()


#endregion


#region MAIN PROGRAM
if __name__ == '__main__':
    main()
#endregion


#region END PROGRAM
clear_screen()
log_out_screen()
wait_for_user()
#endregion