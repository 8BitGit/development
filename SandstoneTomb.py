print('welcome to the sandstone tomb.')


def part4():
    print('\nYou continue of the corner of the room, where you\'ve spotted light.')
    print('With every step you hear the crunch of insects under your bare feet.')
    print('The shadow continues to wave back and fourth as you near the light.')
    print('...suddenly...')
    print('a sigh of relief exits your body as you notice a thicket casting the shadow.')
    print('a thicket from.. Outside.')
    print('Do you run outside? Or go back and look for others?')
    
    continue2 = input('Choose \'first\' or \'second\'.')
    if continue2 == 'first':
        print('\nYou quickly sprint towards the glorious sunlight!')
        print('You\'re almost at the exit when you feel your foot sink into the stone floor slightly.')
        print('This feels almost mechanical.')
        part5()
    elif continue2 == 'second':
        print('You go back into the room and yell loudly for others.')
        print('\'IS ANYONE THERE? I FOUND THE WAY OUT!\'')
        print('Suddenly the sound of rushing air comes from the crack in the wall you saw earlier.')
        print('Millions of bats fly at you, biting and tearing flesh.')
        print('2000 years later, a journalist finds your remains... Most of them.')
        print('Game Over.')
    else:
        continue2 = input('please choose first or second.')
    
    
def part3():
    print('You see a light glowing around the corner.')
    print('However, there are shadows moving around in the light.')
    print('You also notice a passageway in the dark corner of the room.')
    
    way = input('would you like to go down the first or second way?')
    
    if way == 'first':
        part4()
    elif way == 'second':
        print('\nYou continue to the dark corner of the room, craw through the narrow passage...')
        print('You start to hear trembling as you crawl through...')
        print('sand starts to fall from the ceiling...')
        print('2000 years later, archiologists find your body encapsuleated in rubble.')
        print('Game Over.')
    else:
        way = input('Please enter \'first\' or \'second\'.')

def part2():
    print('you find yourself in a dark, dusty room.\nThe sound of millions of bugs crawling around the room echos.\nYou need to get out. And fast.')
    part3()
    
def start_game():
    play = input('would you like to play?')
    if play == 'yes':
        part2()
    else:
        print('You\'ve givin up hope. you die.')
start_game()