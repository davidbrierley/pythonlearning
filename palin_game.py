def palin():
    answer = input('The password is the same forward as it is backward.\n Please input the password: ')

    if (str(answer) == str(answer)[::-1]):
        print('Password correct.')
    else:
        print('Password wrong.')
        palin()

palin()