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


bank_accounts = [
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
    if company['bank_account'] == {}:
        return False
    else:
        return True


def display_account_details(account:dict):
    for account in bank_accounts:
        for key, value in account.items(account):
            if type(key) == dict:
                print(key)
                print(value)
            else:
                print(f'{key} {value}')


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


def print_list_of_dicts(data_list: list) -> None:
    if not data_list:
        print('Lista je prazna')
        return
    
    for index, dictionary in enumerate(data_list, 1):
        print(f'\n')
        print(f'{index}')
        print_dict(dictionary)


def get_valid_input(prompt: str, valid_options: list) -> int:
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_options:
                return choice
            else:
                print(f'Netocan unos, odaberi jednu od opicja {valid_options}')
        except ValueError:
            1





def deposit(bank_account):
    for i, account in enumerate(bank_account, 1):
        print(f'{i}. IBAN: {account['iban']}, Stanje: {account['balance']}')
    
    choice = int(input('Odaberite broj racuna: ')) - 1
    account = bank_account[choice]

    deposit = float(input('Koliko novca zelite uplatit? '))
    account['balance'] += deposit

    transactions.append({
        'amount': deposit,
        'type': 'Uplata',
        'date': datetime.now()
    })


def print_transactions(transactions):
    pass







def main_menu():
    
    print()
    print(f'{"PYBANK":>25}')
    print('=' *50)
    print(f'{"MAIN MENU":>27}')
    print('=' *50)

    print('Izaberi opciju: ')
    print('1. Prikaz informacija racuna')
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
                print_list_of_dicts(bank_accounts)
                wait_for_user()
            elif menu_item == 2:
                create_bank_account(bank_accounts, bank, currency)
                wait_for_user
            elif menu_item == 3:
                print_dict(transactions)
                wait_for_user()
            elif menu_item == 4:
                deposit(bank_accounts)
                wait_for_user()

        else:
            print('Pokrenu funkciju za otvaranje racuna')
            create_bank_account(bank_accounts)
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