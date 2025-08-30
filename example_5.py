class Account:
    def __init__ (self, account_number, owner, balance = 0.0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount >= 0:
            amount = float(input('Enter the amount of money to make a deposit: '))
            self.balance += amount
        else:
            print('Invalid amount')
        
    def withdraw(self, amount):
        amount = float(input('Enter the amount of money to withdraw: '))
        if amount > self.balance:
            print("You don't have enough money to withdraw")
        elif amount == 0:
            print('You cannot withdraw 0')
        elif amount <= self.balance:
            self.balance -= amount
            print(f'You withdrawed {amount}')
            print(f'Your current balance is {self.balance}')
        
    def display(self):
        print(f'Account number is {self.account_number}\n'
              f'Owner of the account is {self.owner}\n'
              f'Your current balance is {self.balance}')
        
class Bank:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = []
    
    def add_account(self, account):
        owner = input('Enter the owner of the account: ')
        account_number = input('Enter the account number: ')
        balance = float(input("Enter the amount of money that you want to make as a first deposit: "))
        self

        Задание: Класс "Банк" и "Счёт"

Создайте два класса:

Класс Account (Счёт)
Атрибуты:

account_number (номер счёта)

owner (владелец счёта)

balance (баланс, по умолчанию 0)

Методы:

deposit(amount) — положить деньги на счёт (увеличивает баланс)

withdraw(amount) — снять деньги со счёта (уменьшает баланс, если хватает средств, иначе выводит сообщение об ошибке)

display() — выводит информацию о счёте (номер, владелец, баланс)

Класс Bank (Банк)
Атрибуты:

name (название банка)

accounts (список счетов, по умолчанию пустой)

Методы:

add_account(account) — добавить новый счёт в банк

remove_account(account_number) — удалить счёт по номеру

get_account(account_number) — вернуть объект счёта по номеру

total_balance() — вернуть сумму всех средств на всех счетах банка

Дополнительно (по желанию):

Добавить проверку, чтобы номера счетов не повторялись в банке.

Сделать метод для перевода денег с одного счёта на другой.

