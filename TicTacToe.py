x = ["°","°","°"]
y = ["°","°","°"]
z = ["°","°","°"]
    
sep = "  +---+---+---"

print("RULES:")
print("Type 2 Numbers between 1-3; The first being the row and the second the column")
print("For exmaple, '1,2' would place here:")

print("    1   2   3")
print("  +-----------")
print("1 | ° | X | °")
print(sep)
print("2 | ° | ° | °")
print(sep)
print("3 | ° | ° | °")

print("")
print("The first to get a row of 3 wins.")

def printit():
    
    print("    1   2   3")
    print("  +---------------------")
    print("1 |",x[0],"|",x[1],"|",x[2])
    print(sep)
    print("2 |",y[0],"|",y[1],"|",y[2])
    print(sep)
    print("3 |",z[0],"|",z[1],"|",z[2]) 
    
def wincheck(sym):
    sym = str(sym)
    win = False
    Stale = False
    i = 0
        
    while i < 3:
        if i == 0:
            c = x
        if i == 1:
            c = y
        if i == 2:
            c = z
        i += 1
        if c[0] == sym and c[1] == sym and c[2] == sym:
            win = True
        
    i = 0
    while i < 3:
        if x[i] == sym and y[i] == sym and z[i] == sym:
            win = True
        i += 1
        
    if x[0] == sym and y[1] == sym and z[2] == sym:
        win = True
    if x[2] == sym and y[1] == sym and z[0] == sym:
        win = True
        
    if H == 9 and win == False:
        print("Stalemate!")
        win = True
        Stale = True
    return(win, Stale)

over = (False, False)
i = 0
H = 0
Stale = False
while over[0] == False:
    a = False
    fakebreak = False
   
    if i % 2 == 0:
        mov = input("Move P1: ")
        sym = "X"
    else:
        mov = input("Move P2: ")
        sym = "O"
    if mov[2] == IndexError:
        indexerror = True
    
    if indexerror == False:
        if mov[0] == "1" and x[int(mov[2])-1] == "°":
            x[int(mov[2])-1] = sym
            a = True
        if mov[0] == "2" and y[int(mov[2])-1] == "°":
            y[int(mov[2])-1] = sym
            a = True
        if mov[0] == "3" and z[int(mov[2])-1] == "°":
            z[int(mov[2])-1] = sym
            a = True
    
    if a == False:
        print("That's not a valid move.")
    
    if a == True:
        i += 1
        H += 1
        printit()
    over = wincheck(sym)

if sym == "X" and over[1] == False:
    print("Player 1 wins!")
if sym == "O" and over[1] == False:
    print("Player 2 wins!")
