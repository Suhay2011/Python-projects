#implimentation of Tic-Tac-Toe game in python

'''We will make the board using dictionary 
   in which keys will be the location(i.e top-left,mid-right,etc.)
   and initialy it's values will be emty space and then after every move
    we will change the value according to players place of move'''

theBoard = {'7': ' ' ,'8' : ' ','9': ' '
            '4': ' ' ,'5' : ' ','6': ' '
            '1': ' ' ,'2' : ' ','3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(keys)

'''We will have to print the updated board sfter every move in the game and thus we will make a function in which we'll defint the printBoard function ao that we can easily print the board by calling this function.'''

def printBoard(board):
    print(board['7'] + '|'board['8'] + '|' board['9'])
    print('-+-+-')
    print(board['4'] + '|'board['5'] + '|' board['6'])
    print('-+-+-')
    print(board['1'] + '|'board['2'] + '|' board['3'])

#now we'll write the main function which has all the game functionality
def game():

    turn = "X"
    count = "0"


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn" + turn + "Move to which place?")

        move = input()

        if theBoard[move] ==' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is alreddy filled.\n Move to which place")
            continue

        #now we will if playyer X or O ahs won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':#across the top
                printBoard(theBoard)
                print(\nGame Over.\n)
                print(" **** "+turn + "Won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': #diagonal
                printBoard(theBoard)
                print(\nGame Over.\n)
                print(" **** "+turn + "Won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': #diagonal