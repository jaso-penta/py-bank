
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


bank_accounts = []


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
    if company['bank_account'] == []:
        print("Nema kreiranih bankovnih računa. Molimo prvo kreirajte račun.")
        wait_for_user()
        return False
    else:
        return True


def show_bank_account(bank_accounts):
    for account in bank_accounts:
        for key, value in account.items(bank_accounts):

            if type(value) == dict:
                print()
                print(f'{key}')
                print(f'{value}')    
            
            else:
                row =  f'{key.upper()} {value}'
                print(row)



def main_menu():
    
    print()
    print(f'{"PYBANK":>25}')
    print('=' *50)
    print(f'{"MAIN MENU":>27}')
    print('=' *50)

    print('Izaberi opciju: ')
    print('1. Prikaz detalje bankovnog racuna')
    print('2. Kreiraj novi racun')
    print('3. Prikaz transakcija')
    print('4. Uplata sredstava')
    print('5. Isplata sredstava')
    print('6. Prikaz podataka o vlasniku racuna')
    print('0. EXIT')

    return get_valid_input('Upisite broj ispred akcije koju zelite pokrenuti: ', list(range(6)))


def main():
    while True:
        if company_has_account():
            menu_item = main_menu()

            if menu_item == 0:
                return
            elif menu_item == 1:
                show_bank_account(bank_accounts)
                wait_for_user()

            elif menu_item == 2:
               create_new_account()
               wait_for_user()
            elif menu_item == 3:
               
                wait_for_user()
            elif menu_item == 4:
               
                wait_for_user()

        else:
            print('Pokrenu funkciju za otvaranje racuna')
            create_new_account()
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