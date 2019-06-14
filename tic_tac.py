from IPython.display import clear_output

print('Welcome to Tic Tac Toe!', '\n')

while True:

    # printing board
    data = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


    def new_board(x, y, z):
        global data
        data[x][y] = z
        hr = "-----------"
        clear_output()
        print('  {a} | {b} | {c} '.format(a=data[0][0], b=data[0][1], c=data[0][2]), '\n', hr)
        print('  {d} | {e} | {f} '.format(d=data[1][0], e=data[1][1], f=data[1][2]), '\n', hr)
        print('  {g} | {h} | {i} '.format(g=data[2][0], h=data[2][1], i=data[2][2]))


    # move validation check
    done_moves = []


    def move_check(player1_list):
        global done_moves
        if player1_list in done_moves:
            player1_ask = input('This place is already occupied. Please enter another move: ')
            player1_list = player1_ask.split(',')
            return move_check(player1_list)
        else:
            m = int(player1_list[0]) - 1
            n = int(player1_list[1]) - 1
            if m not in range(0, 3) or n not in range(0, 3):
                player1_ask = input('This move is out of board range. Please enter another move: ')
                player1_list = player1_ask.split(',')
                return move_check(player1_list)
            else:
                done_moves.append(player1_list)
                return [m, n]


    # winner check


    def winner_check(data, sign):
        for i in range(0, 3):
            return ((data[i][0] == data[i][1] == data[i][2] == sign) or  # horizontals
                    (data[0][i] == data[1][i] == data[2][i] == sign) or  # verticals
                    (data[0][0] == data[1][1] == data[2][2] == sign) or  # diagonal1
                    (data[0][2] == data[1][1] == data[2][0] == sign))  # diagonal2


    # taking positions of players' move


    def player_move(sign):
        player1_ask = input("Next player turn! Please enter your move position separated by ',' i.e. row,column: ").lower()
        player1_list = player1_ask.split(',')
        move = move_check(player1_list)
        new_board(move[0], move[1], sign)


    # taking sign choice of first player
    sign1 = ''
    while not (sign1 == 'o' or sign1 == 'x'):
        input1 = input(
            "Hey! You got the first move of the game. Chose your sign 'o' or 'x' and position of your first move "
            "separated by ',' i.e. sign,row,column: ")
        list1 = input1.split(',')
        sign1 = list1[0]

    move_list = list1[1::]
    first_move = move_check(move_list)
    new_board(first_move[0], first_move[1], sign1)
    if sign1 == 'o':
        sign2 = 'x'
    else:
        sign2 = 'o'

    # continuing game
    for i in range(1, 9):
        if i % 2 == 0:
            player_move(sign1)
            if winner_check(data, sign1):
                print('\n', '!!! PLAYER_1 WINS !!!')
                break
        else:
            player_move(sign2)
            if winner_check(data, sign2):
                print('\n', '!!! PLAYER_2 WINS !!!')
                break
    if i == 8:
        print("Oops! It's a draw.")

        # asking user if he wants to play again or not
    print('\n')
    choice = input("If you want to play again enter 'Y': ").upper()
    if choice != 'Y':
        break
