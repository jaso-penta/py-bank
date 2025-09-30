#region IMPORTS


#endregion


#region INIT DATA
import os
from posixpath import ismount
from datetime import datetime


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

bank_account = {
    'id': 1,
    'account_number': '78799812',
    'iban': 'HR45875465481354654',
    'balance': 0.00,
    'opening_date': '2025-09-29',
    'bank': bank,
    'currency': currency,
    'transactions': transactions
}

#endregion


#region FUNCTIONS
def clear_screen():
    os.system('clear')



def payment(bank_account):
    while True:
        pay = input('\nUpisite iznos koji zelite uplatiti (ili "exit" za nastavak u main menu): ')

        if pay.lower() == 'exit':
            print('Uplata otkazana.')
            return False

        ammount = float(pay)
        if ammount <= 0:
            print('Iznos mora biti veci od 0 €, upisi exit za izlazak')
            continue
        
        
        transaction = {
                'type': 'UPLATA',
                'amount': ammount,
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'balance_after': bank_account['balance'] + ammount
            }

        bank_account[transactions].append(transaction)


        bank_account['balance'] += ammount
        print(f'Uplaceno: {ammount} EUR | Novo stanje: {bank_account['balance']} EUR')
        return True
    



def has_bank_account(company, bank_account):
    if company['id'] == bank_account['id']:
        print(f'\nFirma {company['name']} ima bankovni racun.')
        print(f'Broj racuna je {bank_account['account_number']}\n')
        if bank_account['balance'] < 500.00:
            print('Iznos na racunu nije dovoljan:',bank_account['balance'],'€' ' \nPotrebno stanje na racunu je min 500 €')
            payment(bank_account)
        else:
             print(f"Stanje na racunu je dovoljno: {bank_account['balance']} EUR")

        input('Za nastavak pritisnite ENTER')
    

    else:
        print('Firma nema bankovni racun, potrebno otvoriti racun')
    



def bank_account_info(bank_account):
     print(f"IZNOS:{bank_account['balance']}€\nID: {bank_account['id']}\nBroj racuna: {bank_account['account_number']}\nIBAN: {bank_account['iban']}\nDATUM OTVARANJA:{bank_account['opening_date']}\nBANKA: {bank_account['bank']['name']}")



#endregion


#endregion

#region GUI
def main_menu():
    while True:
        print()
        print(f'{"PYBANK":>25}')
        print('=' *50)
        print(f'{"MAIN MENU":>27}')
        print('=' *50)

        print('Izaberi opciju: ')
        print('1. Prikaz racuna i stanja')
        print('2. Kreiraj novi racun')
        print('3. Informacije o racunu')
        print('4. Prikaz transakcija')
        print('5. Uplata sredstava')
        print('6. Isplata sredstava')
        print('7. Prikaz podataka o vlasniku racuna')
        print('0. EXIT')
        
        menu_item = input('Upisite broj ispred funkcionalnosti koju zelite napraviti: ')

        if menu_item.isdigit():
            return int(menu_item)
        else:
            print('Neispravan unos, pokusajte ponovno.')
            input('Za novi izbor pritisnite ENTER')
#endregion


#region MAIN PROGRAM
def main():
    has_bank_account(company, bank_account)
    while True:
        menu_item = main_menu()

        if menu_item == 0:
            return
        elif menu_item == 1:
            pass
        elif menu_item == 2:
            pass
        elif menu_item == 3:
            print()
            bank_account_info(bank_account)
            print()
            input('Za nastavak pritisnite ENTER')
        elif menu_item == 4:
            pass
        elif menu_item == 5:
            print()
            payment(bank_account)
            print()
            input('Za nastavak pritisnite ENTER')

            
        

        


if __name__ == '__main__':
    main()
#endregion

#region END PROGRAM
print()
print('Hvala i dovidjenja')
print()
#endregion