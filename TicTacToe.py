
def printBoard(board):
    for items in board:
        print(items)

def checkBoard (shape):
    #Checks for Horizontals
    for rows in range(len(board)):
        counter = 0;
        for col in range(len(board[rows])):
            if(board[rows][col] == shape):
                counter += 1
                if counter == 3:
                    print("Game is over")
                    if(shape == "X"):
                        print("Player 1 has won!")
                    else:
                        print("Player 2 has won!")

                    return False
            else:
                counter = 0
     #Checks for Verticals
    # is equal to 1 because the loop if statement will go through
    for rows in range(len(board)):
        counter = 0
        for col in range(len(board[rows])):
            if (board[col][rows] == shape):
                counter += 1
                if counter == 3:
                    print("Game is over")
                    if (shape == "X"):
                        print("Player 1 has won!")
                    else:
                        print("Player 2 has won!")

                    return False
            else:
                    counter = 0

    for rows in range(len(board) - 2):
        for col in range(len(board[rows]) - 2):
            if (board[rows][col] == board[rows + 1][col + 1] and board[rows][col] == board[rows + 2][col + 2] and
                        board[rows][col] == shape):
                print("Game is over")
                if (shape == "X"):
                    print("Player 1 has won!")
                else:
                    print("Player 2 has won!")
                return False

    for rows in range(len(board) - 1, 0, -1):  # start out at the last row
        for col in range(len(board[rows]) - 2):  # Starts out at the first column
            if board[rows][col] == board[rows - 1][col + 1] and board[rows][col] == board[rows - 2][col + 2] and \
                            board[rows][col] == shape:
                print("Game is over")
                if (shape == "X"):
                    print("Player 1 has won!")
                else:
                    print("Player 2 has won!")
                return False
    return True

def spaceChecker():
    for rows in range(len(board)):
        for col in range(len(board[rows])):
            if board[rows][col] == "":
                return True
    return False

def gamePlay():
    gameNotOver = True
    emptySpaces = True

    while gameNotOver:
        player1RowInput = int(input("Player 1: Which row would you like to choose? (1-3)"))
        player1ColInput = int(input("Player 1: Which column would you like to choose? (1-3)?"))

        while( (player1RowInput) > 3 or (player1RowInput <  1) or (player1ColInput > 3 or player1ColInput < 1 )):
            print("Sorry! One or more inputs are not within 1 and 3!")
            player1RowInput = int(input("Player 1: Which row would you like to choose? (1-3)"))
            player1ColInput = int(input("Player 1: Which column would you like to choose? (1-3)?"))

        validMove = (board[player1RowInput - 1][player1ColInput - 1] == '')


        while not validMove:
            print("Invalid Move: Space Already Occupied")
            player1RowInput = input("Player 1: Which row would you like to choose? (1-3)")
            player1ColInput = input("Player 1: Which column would you like to choose? (1-3)?")
            validMove = (board[int(player1ColInput) - 1][int(player1RowInput) - 1] == '')


        board[int(player1RowInput) - 1][int(player1ColInput) - 1] = "X"

        gameNotOver = checkBoard("X")

        printBoard(board)

        if not gameNotOver:
            break

        emptySpaces = spaceChecker()
        if not emptySpaces:
            gameNotOver = False
            print("No winners, the game is a draw")
            break

        player2RowInput = int(input("Player 2: Which row would you like to choose? (1-3)"))
        player2ColInput = int(input("Player 2: Which column would you like to choose? (1-3)?"))

        while ((player2RowInput) > 3 or (player2RowInput < 1) or (player2ColInput > 3 or player2ColInput < 1)):
            print("Sorry! One or more inputs are not within 1 and 3!")
            player2RowInput = int(input("Player 2: Which row would you like to choose? (1-3)"))
            player2ColInput = int(input("Player 2: Which column would you like to choose? (1-3)?"))

        validMove2 = (board[player2RowInput - 1][player2ColInput - 1] == '')

        while not validMove:
            print("Player 2: Invalid Move: Space Already Occupied")
            player2RowInput = input("Player 2: Which row would you like to choose? (1-3)")
            player2ColInput = input("Player 2: Which column would you like to choose? (1-3)?")
            validMove2 = (board[int(player2ColInput) - 1][int(player2RowInput) - 1] == '')


        board[int(player2RowInput) - 1][int(player2ColInput) - 1] = "O"

        gameNotOver = checkBoard("O")

        printBoard(board)

        if not gameNotOver:
            break

        emptySpaces = spaceChecker()
        if not emptySpaces:
            gameNotOver = False
            print("No winners, the game is a draw")
            break

if __name__ == '__main__':
    gameNotOver = True
    emptySpaces = True
    board = [ ["","",""],
        ["","",""],
        ["","",""] ]
    printBoard(board)

    while gameNotOver:
        player1RowInput = int(input("Player 1: Which row would you like to choose? (1-3)"))
        player1ColInput = int(input("Player 1: Which column would you like to choose? (1-3)?"))

        while( (player1RowInput) > 3 or (player1RowInput <  1) or (player1ColInput > 3 or player1ColInput < 1 )):
            print("Sorry! One or more inputs are not within 1 and 3!")
            player1RowInput = int(input("Player 1: Which row would you like to choose? (1-3)"))
            player1ColInput = int(input("Player 1: Which column would you like to choose? (1-3)?"))

        validMove = (board[player1RowInput - 1][player1ColInput - 1] == '')


        while not validMove:
            print("Invalid Move: Space Already Occupied")
            player1RowInput = input("Player 1: Which row would you like to choose? (1-3)")
            player1ColInput = input("Player 1: Which column would you like to choose? (1-3)?")
            validMove = (board[int(player1ColInput) - 1][int(player1RowInput) - 1] == '')


        board[int(player1RowInput) - 1][int(player1ColInput) - 1] = "X"

        gameNotOver = checkBoard("X")

        printBoard(board)

        if not gameNotOver:
            break

        emptySpaces = spaceChecker()
        if not emptySpaces:
            gameNotOver = False
            print("No winners, the game is a draw")
            break

        player2RowInput = int(input("Player 2: Which row would you like to choose? (1-3)"))
        player2ColInput = int(input("Player 2: Which column would you like to choose? (1-3)?"))

        while ((player2RowInput) > 3 or (player2RowInput < 1) or (player2ColInput > 3 or player2ColInput < 1)):
            print("Sorry! One or more inputs are not within 1 and 3!")
            player2RowInput = int(input("Player 2: Which row would you like to choose? (1-3)"))
            player2ColInput = int(input("Player 2: Which column would you like to choose? (1-3)?"))

        validMove2 = (board[player2RowInput - 1][player2ColInput - 1] == '')

        while not validMove:
            print("Player 2: Invalid Move: Space Already Occupied")
            player2RowInput = input("Player 2: Which row would you like to choose? (1-3)")
            player2ColInput = input("Player 2: Which column would you like to choose? (1-3)?")
            validMove2 = (board[int(player2ColInput) - 1][int(player2RowInput) - 1] == '')


        board[int(player2RowInput) - 1][int(player2ColInput) - 1] = "O"

        gameNotOver = checkBoard("O")

        printBoard(board)

        if not gameNotOver:
            break

        emptySpaces = spaceChecker()
        if not emptySpaces:
            gameNotOver = False
            print("No winners, the game is a draw")
            break


    print("Thanks for playing!!!")








