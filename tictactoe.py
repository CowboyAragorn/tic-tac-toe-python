theBoard = {'top-L':' ', 'top-M':' ','top-R':' ',
            'mid-L': ' ', 'mid-M':' ', 'mid-R':' ',
            'bot-L':' ', 'bot-M':' ', 'bot-R':' '}

def printBoard(board):
    print(board['top-L'] +'|'+board['top-M']+'|'+board['top-R'])
    print('-+-+-')
    print(board['mid-L'] +'|'+board['mid-M']+'|'+board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] +'|'+board['bot-M']+'|'+board['bot-R'])

def checkWin(board):
    winCombinations = [
        [board['top-L'],board['top-M'],board['top-R']],
        [board['mid-L'],board['mid-M'],board['mid-R']],
        [board['bot-L'],board['bot-M'],board['bot-R']],
        [board['top-L'],board['mid-L'],board['bot-L']],
        [board['top-M'],board['mid-M'],board['bot-M']],
        [board['top-R'],board['mid-R'],board['bot-R']],
        [board['top-L'],board['mid-M'],board['bot-R']],
        [board['top-R'],board['mid-M'],board['bot-L']],
                       ]
    for i in range(len(winCombinations)):
        if winCombinations[i] == ['X','X','X']:
            printBoard(theBoard)
            print('X won! Congrats!')
            return True
        elif winCombinations[i] == ['O','O','O']:
            printBoard(theBoard)
            print('O won! Congrats!')
            return True

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    #choose a space to play, if one is taken, make user rechoose
    while True:
        move = input()
        if theBoard[move] != ' ':
            print('That space is already taken, choose another:')
            continue
        theBoard[move] = turn
        break
      #check if victory has been achieved
    if checkWin(theBoard):
        break
    #else switch turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    #in cat scenario
    if i==8:
        printBoard(theBoard)
        print('CAT! - Game over')


