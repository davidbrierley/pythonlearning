#given_number = input('Please Enter Pin ')

def atm_machine(pin_number, withdraw_amount, balance):

    given_number = input('Please Enter Pin ')

    if pin_number == int(given_number) and withdraw_amount <= balance:
        print('Please take your money.')
        balance -= withdraw_amount
        print('Your Balance is {}'.format(balance))
    elif pin_number == int(given_number):
        print('Pin Number is not correct. Please try again!')
    elif balance == 0:
        print('Your Balance is empty.')
    elif pin_number == int(given_number) and withdraw_amount > balance:
        print('Your Balance is too low.')
        print('Your current Balance is {}'.format(balance))
    else:
        print('Error')
        atm_machine()

atm_machine(1234,130,250)