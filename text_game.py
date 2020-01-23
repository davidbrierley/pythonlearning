from time import sleep
import random

GREEN =  '\033[32m' #32m changes to green
RED = '\033[31m'    #31m red
BLUE = '\033[34m'   #34m blue
PURPLE = '\033[35m' #35m purple
WHITE = '\033[37m'  #37m white

#         / brown door
# wake up | steel door
#         \ green door

def fac_hallway():
    print('______________________________________________')
    print(RED + 'Which room do you enter?')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: A brown rusty door:')
    sleep(1)
    print('B: A steel door with a broken padlock hanging from it:')
    sleep(1)
    print('C: A wooden green door with claw marks across the front:')
    sleep(1)
    print('______________________________________________')
    answer = input('Only Answer A/B/C: ')

    if answer.lower().strip() == 'a':
        brown_door()
    elif answer.lower().strip() == 'b':
        steel_door()
    elif answer.lower().strip() == 'c':
        sleep(1)
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        sleep(1)
        print('You open the wooden green door and see nothing.')
        green_door()
    else:
        print('______________________________________________')
        print('You stand awkwardly.')
        fac_hallway()

# brown door | memory | factory floor

def brown_door():
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('Memory: Walking into the room you feel very warm and happy, this room is familiar to you.')
    sleep(1)
    print('You remember your childhood and what makes you so special.')
    sleep(1)
    print('')
    main_factory()

#             / open bag | factory floor
# steel door |
#             \ not open bag | factory floor

def steel_door():
    sleep(1)
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('You look around room and find a bag in the corner of the room.')
    sleep(1)
    print('______________________________________________')
    print(RED + 'Do you open the bag?')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Yes I want to open the bag:')
    sleep(1)
    print('B: No I will leave the bag alone:')
    answer = input('Only Answer A/B: ')

    if answer.lower().strip() == 'a':
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        print('You open the bag to find a hole in the bottom.')
        sleep(1)
        print('You look around the room more.')
        sleep(1)
        print('Suddenly a ray of light comes from a open door you walk through and see you\'re in the main factory room.\n')
        main_factory()
    elif answer.lower().strip() == 'b':
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        print('You look around the room more.')
        sleep(1)
        print('Suddenly a ray of light comes from a open door you walk through and see you\'re in the main factory room.\n')
        main_factory()
    else:
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        print('standing infront of the bag you wonder whats inside.')
        center_door()

# green door | dead end

def green_door():
    print('______________________________________________')
    print(RED + 'Which room do you enter?')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: A brown rusty door:')
    sleep(1)
    print('B: A steel door with a broken padlock hanging from it:')
    sleep(1)
    print('______________________________________________')
    answer = input('Only Answer A/B: ')

    if answer.lower().strip() == 'a':
        brown_door()
    elif answer.lower().strip() == 'b':
        steel_door()
    else:
        print('______________________________________________')
        print('You stand awkwardly.')
        fac_hallway()

#              / crawl in machinary
# main factory |
#              \ crack in wall

def main_factory():
    print(WHITE + 'The room contained alot of machinery \'the place appears to be a logging factory\' you think judging \nthe rusting saws and chopped tree trunks.')
    sleep(2)
    print('Broken glass and rubbish littered the floor, you try to see a path past the machines but it was like a maze.')
    sleep(2)
    print('______________________________________________')
    print(RED + 'Do you crawl through the manchinary or Do you find another way round.')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Crawl through machine: ')
    sleep(1)
    print('B: Find way round: ')
    print('______________________________________________')
    answer = input('Only Answer A/B: ')

    if answer.lower().strip() == 'a':
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        print('You start to climb over the conveyor belts and metal pipes, The tinkling of glass being shifted suddenly to \nyour right tickles you and a scratching sound like a sharp object on metal.')
        sleep(2)
        print('You freeze looking for the source of the sound but it all was silent now, you start to move forward again')
        sleep(2)
        print('Suddenly theres a blaring horn sound and steam rises from the metal around you, the conveyor belt you are on \nclanks into life and starts drifting you towards a rotating saw.')
        sleep(2)
        print('There was a second conveyor belt next you, metal chains also passed over your head attached to a moving track \non the roof.\n')
        sleep(6)
        for x in range(1):
            chance = (random.randint(1,100))

            if chance > 35:
                print('You jump up and grab the next chain that passes over you and it swings to the right avoiding the saw.')
                sleep(1)
                print('You pass over clunking machinery looking for a place to jump off and spy a flat platform coming up on your left.')
                sleep(1)
                print('You swing back and forth on the chain timing it to swing left as the platform came up and landed but stumbled on it.')
                sleep(1)
                print('There was a ladder up to a balcony which seemed to be a second floor which you take.\n')
                sleep(1)
                fac_corridor()
            else:
                print('You jump onto the conveyor belt next to you thats going in the opposite direction but your feet go sideways under you and you are swept into a shredding machine')
                sleep(2)
                print('You Died')
                cont_train()
    elif answer.lower().strip() == 'b':
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        sleep(1)
        print('You find a crack in the wall with a set of stairs leading down to a room half flooded with steam pipes covering the roof.')
        pipe_flood()
    else:
        print('Awkward Silence.')
        main_factory()

#                  / office | basement
# factory corridor |
#                  \ kitchen | basement

def fac_corridor():
    sleep(2)
    print('reaching the 2nd floor you enter a corridor on the left is a living room with 3 photos on the wall')
    sleep(2)
    print('and on the right is a kitchen with broken ovens and walls burnt black.')
    sleep(2)
    print('______________________________________________')
    print(RED + 'Do you enter the office or the kitchen? ')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Enter the Office:')
    sleep(1)
    print('B: Enter the Kitchen:')
    sleep(1)
    answer = input('Only Answer A/B: ')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')

    if answer.lower().strip() == 'a':
        print('Entering the office you see 3 portraits on the wall, 2 of them with a big' + RED + ' X ' + WHITE + 'and the last with a circle,')
        sleep(2)
        print('next to the portraits is a mirror, you gaze into the mirror and realise the portrait that is circled is YOU!\n')
        sleep(2)
        print('looking in the mirror you notice a shadow appearing from the corner of the room.\n')
        sleep(2)
        print('you instantly run towards the corridor, you hear a creak as the floor breaks under you, as you fall to the basement')
        sleep(2)
        print('you see the shadowy figure looking over the hole you fell through, as you\'re about to make out the shadows face you hit the water that is flooding the basement')
        flood_basement()

    elif answer.lower().strip() == 'b':
        print('Entering the kitchen you smell a strong scent of coffee.')
        sleep(2)
        print('looking around you notice a shadow appearing from the corner of the room.\n')
        sleep(2)
        print('you instantly run towards the corridor, you hear a creak as the floor breaks under you, as you fall to the basement')
        sleep(2)
        print('you see the shadowy figure looking over the hole you fell through, as you\'re about to make out the \nshadows face you hit the water that is flooding the basement')
        flood_basement()
    else:
        print('Which room to choose.')
        fac_corridor()

#          / tunnel | life
# basement |
#          \ cave | die

def flood_basement():
    print('______________________________________________')
    print(RED + 'Do you enter the tunnel or the cave?')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Enter Tunnel:')
    sleep(1)
    print('B: Enter Cave:')
    sleep(1)
    answer = input('Only Answer A/B: ')
    if answer.lower().strip() == 'a':
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        sleep(1)
        print('Stepping into the tunnel you are greeted with thick webbing')
        sleep(1)
        tunnel_web()
    elif answer.lower().strip() == 'b':
        print('______________________________________________')
        print(RED + 'YOU DIED!')
        print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        cont_train()
    else:
        print('Standing on the roof you feel conflicted.')
        flood_basement()

def tunnel_web():
    print('______________________________________________')
    print(RED + 'Do you want to pick up the stick and hit the webs?')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Pick up the stick and hit webbing:')
    sleep(1)
    print('B: Hit the web with your hand:')
    invent =[
    ''
    ]
    attack=(random.randint(1,100))
    answer = input('Only Answer A/B: ')
    if answer.lower().strip() == 'a':
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        sleep(1)
        print('You pick up the stick')
        invent.append('stick')
        if 'stick' in invent :
            print('You swing at the webbing.')
            if attack >= 50:
                sleep(3.0)
                print("Webbing destroyed.")
                elevator_act()
            elif attack < 49:
                sleep(2.0)
                print("You miss and fall into the webbing, spiders crawl all over your body as you suffocate.")
                print('______________________________________________')
                print(RED + 'YOU DIED!')
                print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
                cont_train()
    else:
        sleep(2.0)
        print("You miss and fall into the webbing, spiders crawl all over your body as you suffocate.")
        print('______________________________________________')
        print(RED + 'YOU DIED!')
        print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        cont_train()

#          / pull lever | garden 
# evelator |
#          \ leave lever | die

def elevator_act():
    print('______________________________________________')
    print(RED + 'Do you want to activate the elevator.')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Yes pull the lever:')
    sleep(1)
    print('B: No I will not pull the lever:')
    answer = input('Only Answer A/B: ')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    if answer.lower().strip() == 'a':
        print('Pulling the lever makes the whole elevator light up, "bing! going up" you quickly get on and press a random button.')
        house_garden()
    elif answer.lower().strip() == 'b':
        print('You step away from the elevator when suddenly a claw flys out from the shadows and stabs you. You Died!')
        cont_train()
    else:
        print('Standing at the elevator, You wonder if it will work.')
        elevator_act() 

#        / break gate | freedom
# garden | 
#        \ climb fence | die

def house_garden():
    print('______________________________________________')
    print(RED + 'Break garden lock or climb over steel fence.')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Break the lock with force:')
    sleep(1)
    print('B: Climb over the fence:')
    sleep(1)
    answer = input('Only Answer A/B: ')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    if answer.lower().strip() == 'a':
        print('Once the gate is broken open you run through the fields facing, coming to a small town with a bus terminal.')
        freedom_win()
    elif answer.lower().strip() == 'b':
        print('You climb onto the fence and slip impaling yourself on the top as you slide down bleeding out. You Died!')
        cont_train()
    else:
        print('The gate looks breakable.')
        house_garden()

def freedom_win():
    print('You get on the bus to freedom and never look back.')
    sleep(1)
    print('______________________________________________')
    print('YOU WIN!')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    cont_train()

#            / dive | train
# flood pipe |
#            \ climb | password

def pipe_flood():
    print('looking around you see a ladder going to the next floor, you also see a hole in the floor with light shining from it.')
    sleep(1)
    print('The hole is filled with water and must dive under to reach the other side.')
    sleep(1)
    print('______________________________________________')
    print(RED + 'Do you dive under or Climb the ladder.')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Dive under:')
    sleep(1)
    print('B: Climb the ladder:')
    sleep(1)
    answer = input('Only Answer A/B: ')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    if answer.lower().strip() == 'a':
        print('Diving under the water you realise you are now outide the factory walls and free in the distance you see an \nabandoned train station.')
        sleep(1)
        print('Waiting at train station a train arrives and you get on it.')
        train_cart()
    elif answer.lower().strip() == 'b':
        print('You climbed to the ladder and see a steel gate with stairs behind them.')
        sleep(1)
        print('You approach the gate and it has a keypas asking for a password.\n')
        palin()
    else:
        print('Your clothes feel wet.')
        pipe_flood()

# password | palindrome | roof

def palin():
    answer = input('The password is the same forward as it is backward, can be word or number or any length \nPlease input the password: ')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    if (str(answer) == str(answer)[::-1]):
        print('Password correct.')
        fac_roof()
    else:
        print('Password wrong.')
        palin()

#      / down | dodge
# roof | 
#      \ stay | die

def fac_roof():
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(0.5)
    print('Once on the roof you feel the floor crumble beneth you, as you move back a shadowy figure crashes through the roof making a big hole')
    sleep(1)
    print('The beast is blinded by the light and collapses and falls into the main factory hall, crashing into industrial machinary.\n')
    sleep(1)
    print('You remember that there is a lever to restart the machine trapping the beast and killing it.\n')
    sleep(1)
    print('______________________________________________')
    print(RED + 'Do you go down and pull the lever or stay on the roof')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Go down to the lever:')
    sleep(1)
    print('B: Stay on the roof:')
    sleep(1)
    print('______________________________________________')
    answer = input('Only Answer A/B: ')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    if answer.lower().strip() == 'a':
        dodge()
    elif answer.lower().strip() == 'b':
        print('You have a sudden bout of vertigo, causing you to trip and fall off of the roof, the beast opens it\'s mouth and you fall in and get eaten. You Died.')
        cont_train()
    else:
        print('Standing on the roof you feel conflicted.')
        fac_roof()

#       / left | lever | win
# dodge |
#       \ right | control

def dodge():
    sleep(1)
    print('Climbing down, The beast jumps infront of you blocking your way!')
    sleep(1)
    print('______________________________________________')
    print(RED + 'Do you dodge left or right')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Dodge left towards the lever:')
    sleep(1)
    print('B: Dodge right away from the lever:')
    sleep(1)
    answer = input('Only Answer A/B: ')
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    if answer.lower().strip() == 'a':
        print('You dodge left reaching the lever and pull it, which traps the beasts tail. ')
        print('                                              ')
        print('The beast screams in agony as it is dragged into machine and its ultimate demise.')
        print('______________________________________________')
        print('YOU WIN!')
        print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    elif answer.lower().strip() == 'b':
        print('you dodge right away from the lever making it safely into a control room.')
        sleep(1)
        print('you find a crank system on the wall, you turn it and it suddenly snaps, bringing tons of logs on top of the beast killing it.')
    else:
        print('You didn\'t dodge')
        print('______________________________________________')
        print(RED + 'YOU DIED!')
        print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        cont_train() 

#            / stay | die
# train cart |
#            \ jump | die

def train_cart():
    print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(2)
    print('A short time after leaving a big crashing sound comes from the back of the train, its the shadowy figure \nyou can now see what has been stalking you, it is a beast with four arms and a big snout.')
    sleep(1)
    print('______________________________________________')
    print(RED + 'Do you face it or jump off the train and escape.')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    sleep(1)
    print('A: Face your fears:')
    sleep(1)
    print('B: Jump off the train:')
    sleep(1)
    answer = input('Only Answer A/B: ')
    if answer == 'a':
        print('You turn to jump but you get scared, the beast roars and slashes your back. ')
        print('______________________________________________')
        print(RED + 'YOU DIED!')
        print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        cont_train()    
    elif answer == 'b':
        print('You turn and jump off the train as the beast slashes and misses you by inches, you land breaking both legs and faceplanting.')
        print('______________________________________________')
        print(RED + 'YOU DIED!')
        print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
        cont_train()
    else:
        print('Make a choice.')
        train_cart()

# continue death

def cont_train():
    print('______________________________________________')
    print(RED + 'Do you wish to restart.')
    print(WHITE + '¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
    answer = input('Only Answer A/B: ')
    if answer.lower().strip() == 'a':
        fac_hallway()
    elif answer.lower().strip() == 'b':
        exit()

print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')
sleep(0.1)
print('##########################################################')
sleep(0.1)
print('    _______ __                       __           __ ')
sleep(0.2)
print('   |     __|  |_.----.---.-.-----.--|  |.-----.--|  |')
sleep(0.2)
print('   |__     |   _|   _|  _  |     |  _  ||  -__|  _  |')
sleep(0.2)
print('   |_______|____|__| |___._|__|__|_____||_____|_____|')
sleep(0.2)
print('')
sleep(0.1)
print('###########################################################')
sleep(0.2)
print('____________________________________________________________')
sleep(0.2)
print('')
print(WHITE + 'You wake up in a barren sandy landscape almost like a beach with no sea, infront of you')
sleep(2.5)
print('lies several buildings with looming spire like chimneys, you realise that it is a factory.\n')
sleep(2.5)
print('Several questions are brought to your mind, who am I, why am I here and what is this place?')
sleep(2.5)
print('There appears to be nothing around for miles, which enticed one option. Enter the factory.\n')
sleep(2.5)
print('Silent throughout the building besides the creaking of metal structures.')
sleep(2.5)
print('You enter and are met with a hallway with three rooms leading off it.')
sleep(1)

fac_hallway()