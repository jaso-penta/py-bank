
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


def get_valid_input(prompt:str, valid_option: list):
    while True:
        choice = int(input(prompt))
        try:
            if choice in valid_option:
                return choice
            else:
                print(f'Netocan unos, birajte izmedju {valid_option}')
        except ValueError:
            print('Greska, morate unjeti broj')


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


def create_bank_account(account):
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
    


    account = {}
    account['id'] = input('Unesi ID: ')
    account['iban'] = input('Unesite IBAN ')
    account['balance']= deposit
    account['opening_date']= today
    account['bank'] = bank
    account['currency'] = currency
    account['transactions'] = transactions

    bank_accounts.append(account)
    print()
    next_account = input('Zelite li unijeti novi kontakt? (Da/Ne): ')
    print()
    if next_account.lower() != 'da':
        return

    return account


def in_deposit(bank_accounts: list, transactions: list):
    for i, account in enumerate(bank_accounts, 1):
        print(f'{i}. {account['iban'], {account['balance']}}: ')

    choice = int(input('Izaberite broj racuna: ')) - 1
    account = bank_accounts[choice]

    deposit_amount = float(input('Unesite zeljeni iznos: '))
    account['balance'] += deposit_amount

    transactions.append({
        'ammount': deposit_amount,
        'type': 'Uplata',
        'date': datetime.now()
    })


def withdraw(bank_accounts: list, transactions: list):
    for i, account in enumerate(bank_accounts, 1):
        print(f'{i}. {account['iban'], {account['balance']}}: ')

    choice = int(input('Izaberite broj racuna: ')) - 1
    account = bank_accounts[choice]

    withdraw_amount = float(input('Unesite zeljeni iznos: '))

    if withdraw_amount > account['balance']:
        print('Nedovoljno sredstava na racunu.')
        return
    
    account['balance'] -= withdraw_amount

    transactions.append({
        'ammount': withdraw_amount,
        'type': 'Isplata',
        'date': datetime.now()
    })

    print(f"Uspješna isplata {withdraw_amount} EUR. Novo stanje: {account['balance']} EUR")
    

def show_transactions(transactions: list):
    for i, transaction in enumerate(transactions, 1):
        print(i) 
        for key, value in transaction.items():
            print(f'{key:<10}: {value:<15}')


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
                clear_screen()
                display_account_details(bank_accounts)
                wait_for_user()
            elif menu_item == 2:
               clear_screen()
               create_bank_account(bank_accounts)
               wait_for_user()
            elif menu_item == 3:
               clear_screen()
               show_transactions(transactions)
               wait_for_user()
            elif menu_item == 4:
                clear_screen()
                in_deposit(bank_accounts, transactions)
                wait_for_user()
            elif menu_item == 5:
                clear_screen()
                withdraw(bank_accounts, transactions)
                wait_for_user()

        else:
            print('Pokrenu funkciju za otvaranje racuna')
            create_bank_account(bank_accounts)
            wait_for_user()
            clear_screen()


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