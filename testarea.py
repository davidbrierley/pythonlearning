import time 

print(' _______ __                       __           __ ')
time.sleep(0.2)
print('|     __|  |_.----.---.-.-----.--|  |.-----.--|  |')
time.sleep(0.2)
print('|__     |   _|   _|  _  |     |  _  ||  -__|  _  |')
time.sleep(0.2)
print('|_______|____|__| |___._|__|__|_____||_____|_____|')
time.sleep(0.6)
print('')
time.sleep(0.2)
print('You awake in a dark place....')
time.sleep(0.5)
print('Looking around you see that you are in an abandoned factory')
time.sleep(0.5)
print('with no memories, You wonder who you are and why you are here.')
time.sleep(0.5)
print('You get up and look for clues, you see a wooden door with a crack in it.')
time.sleep(0.5)
print('')

while True:
    try:
        answer_given = int(input('Do you want to push the door open (push door), or look around the room (look around): '))
    except ValueError:
        print('You stand awkwardly.')
        continue
    else:
        break

if answer_given.lower().strip() == 'push':
    print('')
    time.sleep(0.5)
    print('you push the door as hard as you can')
    time.sleep(0.5)
    print('The door flys open making a big crashing sound')
    time.sleep(0.2)
    answer_given = input('2nd option: ')
    if answer_given.lower().strip() == 'yes':
        print('yes_2')
    else:
        print('no_2')
elif answer_given.lower().strip() == 'look':
    print('You Died')
else:
    print('')