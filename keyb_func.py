import keyboard 
def keyboard_func():  
    if keyboard.is_pressed('up'): 
        print('You Walked North!')
    elif keyboard.is_pressed('down'): 
        print('You Walked South!')
    elif keyboard.is_pressed('left'): 
        print('You Walked West!')
    elif keyboard.is_pressed('right'): 
        print('You Walked East!')
    elif keyboard.is_pressed('a'): 
        print('You Pressed A!')

keyboard_func()