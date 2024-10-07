board = ["°", "°", "°",
         "°", "°", "°",
         "°", "°", "°"]

def printboard(board, sep):
    print("    1   2   3")
    i = 0
    while i < 3:
        lst = ["A", "B", "C"]
        print(lst[i], "|",board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        print(sep)
        i += 1
    
def printrules(linesep):
    print("RULES:")
    print("Type a letter and a number between 1-3; The first being the row and the second the column")
    print("For exmaple, 'A,2' would place here:")

    print("    1   2   3")
    print("  +-----------")
    print("A | ° | X | °")
    print(linesep)
    print("B | ° | ° | °")
    print(linesep)
    print("C | ° | ° | °")

    print("")
    print("The first to get a row of 3 wins.")

def move(board, symbol):
    if symbol == "X": player = "1"
    if symbol == "O": player = "2"
    
    index = checkinput(input("Move Player "+ player+": "))

    while index == "False" or board[index] != "°":
        index = checkinput(input("Invalid move! Pick a letter and a number on the grid corresponding to an empty spot.\nMove Player "+ player +": "))
        
    board[index] = symbol

        
    return(board)
        
def checkinput(inp):
    letters = ["A", "B", "C"]
    numbers = ["1", "2", "3"]    
    i = 0
    
    while i < 2:
        if len(inp) != 2:
            return("False")
        if inp[i] not in letters and inp[i] not in numbers:
            return("False")
        
        if inp[i] in letters:
            letter = letters.index(inp[i])
        if inp[i] in numbers:
            number = numbers.index(inp[i])
        i += 1

    index = number + letter*3
    return(index)

def wincheck(board, symbol):
    i = 0
    n = 0
    while i <7:
        if board[i] == symbol and board[i+1] == symbol and board[i+2] == symbol: return(True)
        if board[n] == symbol and board[n+3] == symbol and board[n+6] == symbol: return(True)
        i += 3
        n += 1
    if board[4] == symbol:
        if board[0] == symbol and board[8] == symbol: return(True)
        if board[2] == symbol and board[6] == symbol: return(True)
    return(False)
    
def gameloop():
    i = 0
    over = False
    Stalemate = False
    linesep = "  +---+---+---"
    printrules(linesep)
    
    while over == False and Stalemate == False:
        
        if i % 2 == 0: symbol = "X"
        else:          symbol = "O"
        
        move(board, symbol)
        printboard(board, linesep)
        over = wincheck(board, symbol)
        if i == 8 and over != True: Stalemate = True
        
        if over == True and symbol == "X": print("Player 1 wins!")
        if over == True and symbol == "O": print("Player 2 wins!")
        if Stalemate == True:              print("Stalemate! No winners today")
        i += 1
        
gameloop()
#ADD BASIC BOT!
