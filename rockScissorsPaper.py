import random


def get_choices():
    options = ('rock', 'paper', 'scissors')
    player = input(f'Enter a choice {options}')
    computer = random.choice(options)
    choices = {'player': player, 'computer': computer}

    return choices


def check_win(player, computer):
    print(f'You chose: {player} , computer chose: {computer}')
    if player == computer:
        return "It's a tie"
    elif player == 'rock':
        if computer == 'scissors':
            return 'Rock smashes scissors! you win'
        else:
            return 'Paper covers rock! you lose'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock! you win'
        else:
            return 'scissors cuts paper! you lose'
    elif player == 'scissors':
        if computer == 'paper':
            return 'scissors cuts paper! you win'
    else:
        return 'Rock smashes scissors! you lose'


choises = get_choices()

result = check_win(choises['player'], choises['computer'])

print(result)
