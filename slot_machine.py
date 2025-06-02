import random
from collections import Counter

def show_balance(balance):
   print('*********************************')
   print(f'Your total balance is {balance: .2f}')
   print('*********************************')

def deposit():
    print('*********************************')
    print('The minimum deposit amount is 10 dollars.')
    amount = float(input('Enter the amount money you want put: '))
    print('*********************************')
    if amount < 10:
        print('*********************************')
        print('You should deposit more' \
        'The minimum deposit amount is 10 dollars.')
        print('*********************************')
    else:
        print('We got your money')
        return amount
    
def withdraw(balance):
    print('*********************************')
    print('The maximum money to withdraw is $100.')
    amount = float(input('Enter the amount to withdraw: '))
    print('*********************************')
    if amount > 100:
        print('*********************************')
        print('It is too much' \
        'The maximum money to withdraw is $100.')
        print('*********************************')
        return 0
    elif amount < 0:
        print('*********************************')
        print('Invalid amount of money')
        print('*********************************')
        return 0
    elif amount > balance:
        print('Insufficient funds')
        return 0
    else:
        return amount

def rules():
    print('*********************************')
    symbols = ['🍒','🍋', '🔔', '💎','7️⃣']
    print('A bet is withdrawn for each game launch (slot spin).')
    print(f'There are these {symbols}')
    print('When you spin the machine, you got 3 symbols')
    print('If you got 2 identical → 2x win')
    print('If you got 3 identical → 5x win')
    print('If you got no identical → losing')
    print('*********************************')

def money(balance):
    launch = float(input('Enter the amount of money for one bet: '))
    if launch > balance:
        print('*********************************')
        print('Insufficient funds')
        print('*********************************')
        return None
    if launch < 0:
        print('*********************************')
        print('Invalid amount of money')
        print('*********************************')
        return None
    else:
        return launch

def game(balance):
    run = True
    while run:
        if balance < 1:
            print('*********************************')
            print('You have no money left to play.')
            print('*********************************')
            break
        bet = money(balance)

        if bet is None:
            continue
        if bet == 0:
            print('Exiting the slot machine...')
            break

        balance -= bet
        
        symbols = ['🍒','🍋', '🔔', '💎','7️⃣']
        sym = random.sample(symbols*3, 3)
        print(f'You got: {sym}')

        counts = Counter(sym)

        if 3 in counts.values():
            win = bet * 5
            balance += win
            print('*********************************')
            print('🎉 JACKPOT! You got 3 matching symbols! 🎉')
            print(f'You win {win}!')
        elif 2 in counts.values():
            win = bet * 2
            balance += win
            print('*********************************')
            print('✨ You got 2 matching symbols! ✨')
            print(f'You win {win}!')
        else:
            print('*********************************')
            print("You lost 😔")
        
        print(f'Your current balance is: {balance: .2f}')
        print('Bet 0 to exit the game')
        print('*********************************')
    return balance

balance = 0
is_running = True

while is_running:
    print('*********************************')
    print('Welcome to the Slot machine!')
    print('1.Show balance')
    print('2.Put money')
    print('3.Withdraw money')
    print("4.Game's rules")
    print('5.Play Slot Machine')
    print('6.Exit')
    print('*********************************')

    choice = input('Enter your choice(1-4): ')
    
    if choice == '1':
        show_balance(balance)
    if choice == '2':
        balance += deposit() 
    if choice == '3':
        balance -= withdraw(balance)
    if choice == '4':
        rules()
    if choice == '5':
        if balance < 1:
            print('*********************************')
            print('Top up your balance first')
            print('*********************************')

        else:
            balance = game(balance)
    if choice == 6:
        is_running = False

print('*********************************')
print('Thank you for the game! See you next time.')
print('*********************************')