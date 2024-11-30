
boarded = [' ' for _ in range(9)]

def show_boarded():
    for index in range(1, 10):
        print(f'{boarded[index - 1]}', end=' ')
        if index % 3 != 0:
            print('|', end=' ')
        if index % 3 == 0 and index < 9:
            print()
            print('- ' * 5)

def check_player1():
    if boarded[0:3] == ['O', 'O', 'O']:
        return True
    elif boarded[3:6] == ['O', 'O', 'O']:
        return True
    elif boarded[6:9] == ['O', 'O', 'O']:
        return True
    elif boarded[0] == 'O' and boarded[4] == 'O' and boarded[8] == 'O':
        return True
    elif boarded[2] == 'O' and boarded[4] == 'O' and boarded[6] == 'O':
        return True
    else:
        return False

def check_player2():
    if boarded[0:3] == ['X', 'X', 'X']:
        return True
    elif boarded[3:6] == ['X', 'X', 'X']:
        return True
    elif boarded[6:9] == ['X', 'X', 'X']:
        return True
    elif boarded[0] == 'X' and boarded[4] == 'X' and boarded[8] == 'X':
        return True
    elif boarded[2] == 'X' and boarded[4] == 'X' and boarded[6] == 'X':
        return True
    else:
        return False


current_spots = [i for i in range(1, 10)]

def start_game():
    print('Welcome to Tic Tac Toe!')
    player1 = input('Player 1, enter your name: ')
    player2 = input('Player 2, enter your name: ')
    
    game_running = True
    player2_turn = True

    while game_running:
        
        while True:
            pos1 = input(f'{player1}, pick a position (1-9): ')
            if pos1.isdigit() and int(pos1) in current_spots:
                current_spots.remove(int(pos1))
                boarded[int(pos1) - 1] = 'O'
                show_boarded()
                if check_player1():
                    print(f'Congratulations {player1}, you won!')
                    game_running = False
                    player2_turn = False
                    break
                else:
                    break
            else:
                print('Invalid choice, try again.')
        
        
        if not current_spots:
            print('It\'s a draw!')
            break

  
        while player2_turn:
            pos2 = input(f'{player2}, pick a position (1-9): ')
            if pos2.isdigit() and int(pos2) in current_spots:
                current_spots.remove(int(pos2))
                boarded[int(pos2) - 1] = 'X'
                show_boarded()
                if check_player2():
                    print(f'Congratulations {player2}, you won!')
                    game_running = False
                    break
                else:
                    break
            else:
                print('Invalid choice, try again.')

start_game()
