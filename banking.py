# Stage 2/4: Luhn algorithm

# Import modules
import random

# Define Luhn-related functions
def checksum(string):
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10

def verify(string):
    return (checksum(string) == 0)

# Define BankingSystem class
class BankingSystem:
    def __init__(self):
        self.card_number = str
        self.card_pin = str
        self.card_dic = {}
        
        self.user_menu_choice = int
    
    def menu(self):
        print('1. Create an account\n2. Log into account\n0. Exit')
        self.user_menu_choice = int(input())
        return self.user_menu_choice
    
    def create_account(self):
        # Credit card generation algorithm
        while True:
            card_number_gen = str(4000000000000000 + random.randint(1000000000, 9999999999))
            if verify(card_number_gen):
                self.card_number = card_number_gen
                break
            else:
                continue
        # PIN generation and dic update
        self.card_pin = str(random.randint(0000,9999)).zfill(4)
        self.card_dic.update({self.card_number: self.card_pin})
        print('')
        print('\nYour card has been created\nYour card number:')
        print(self.card_number)
        print("Your card PIN:")
        print(self.card_pin)
        print('')
        
    def login_account(self):
        user_card_number = input('Enter your card number:\n')
        user_card_pin = input('Enter your PIN:\n')
        
        if user_card_number in [key for key in self.card_dic] and user_card_pin == self.card_dic[user_card_number]:
            print('You have successfully logged in!')
            return 'Successfully'
        else:
            print('Wrong card number or PIN!')
            
    def account_menu(self):
        while True:
            print('''1. Balance\n
            2. Log out\n
            0. Exit''')
            account_menu_choice = int(input())
            
            if account_menu_choice == 1:
                print('\nBalance: 0\n')
            elif account_menu_choice == 2:
                print('You have successfully logged out!')
                break
            else:
                exit()
    
    def main(self):
        while True:
            self.menu()
            if self.user_menu_choice == 1:
                self.create_account()
            elif self.user_menu_choice == 2:
                if self.login_account() == 'Successfully':
                    self.account_menu()
            else:
                print('Bye!')
                break

# Invoke main function
if __name__ == '__main__':
    banking_sys = BankingSystem()
    banking_sys.main()
