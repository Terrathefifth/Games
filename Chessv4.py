"""
pieces0 = [" wRook   ", " wKnight ", " wBishop ", " wQueen  ", " wKing   ", " wBishop ", " wKnight ", " wRook   ",
           " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ",
           "         ", "         ", "         ", "         ", "         ", "         ", "         ", "         ",    
           "         ", "         ", "         ", "         ", "         ", "         ", "         ", "         ",     
           "         ", "         ", "         ", "         ", "         ", "         ", "         ", "         ",     
           "         ", "         ", "         ", "         ", "         ", "         ", "         ", " bRook   ",
           " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ",
           " bRook   ", " bKnight ", " bBishop ", " bQueen  ", " bKing   ", " bBishop ", " bKnight ", " bRook   "]
"""
pieces0 = [" wRook   ", "         ", "         ", "         ", " wKing   ", "         ", "         ", " wRook   ",
           " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ", " wPawn   ",
           "         ", "         ", "         ", "         ", "         ", "         ", "         ", "         ",    
           "         ", "         ", "         ", "         ", "         ", "         ", "         ", "         ",     
           "         ", "         ", "         ", "         ", "         ", "         ", "         ", "         ",     
           "         ", "         ", "         ", "         ", "         ", "         ", "         ", " bRook   ",
           " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ", " bPawn   ",
           " bRook   ", "         ", "         ", "         ", " bKing   ", "         ", "         ", " bRook   "]

hasmoved =  {
    "0": False,        #Whether wRook1 moved
    "4": False,        #Whether wKing  moved
    "7": False,
    
    "56": False,
    "60": False,
    "63": False,
    
    #PAWNS
    "8":  False,
    "9":  False,
    "10": False,
    "11": False,
    "12": False,
    "13": False,
    "14": False,
    "15": False,
    
    "48": False,
    "49": False,
    "50": False,
    "51": False,
    "52": False,
    "53": False,
    "54": False,
    "55": False
}

def printboard(pieces0):
    i = 0
    
    while i < 64:
        row = [str((64-i)//8)]
        print(pieces0[i:i+8] + row)
        print("")
        i += 8    
    col = ["    A    ", "    B    ", "    C    ", "    D    ", "    E    ", "    F    ", "    G    ", "    H    "]
    print(col)

def coordget1(color, type):
    #Asks the user for coordinate. Returns Index of pieces0 and whether that selection is allowed
    if color == "w" or color == "b":
        if color == "w": i = "1"
        if color == "b": i = "2"        
        
        if type == True:
            Pselect = input("Player "+i+ ": Select piece: ")
            alt = True        
        if type == False:
            Pselect = input("Pick destination (r to return): ")
            alt = False
        
    Pindex = coordtranslate(Pselect)
    selection  = isallowed(color, Pindex, alt)
    return(Pindex, selection)

def coordtranslate(Pselect):
    #Takes user input and turns it into index of pieces[0]
    lst = ("A", "B", "C", "D", "E", "F", "G", "H")
    ist = ("1", "2", "3", "4", "5", "6", "7", "8")
    
    if Pselect[0] not in lst or len(Pselect) != 2:
        printboard(pieces0)
        return("False")
    if Pselect[1] not in ist:
        printboard(pieces0)
        return("False")
    

    Pselect = Pselect.replace(Pselect[0], str(lst.index(Pselect[0])))
    Pindex = (int(Pselect[0])+(8-int(Pselect[1]))*8)
    return Pindex

def isallowed(color, Pindex, alt):
    #Checks if a move is allowed
    if Pindex == "False":          return False
    if alt == True:
        check = pieces0[Pindex]
        if check.find(color) == 1 :return True
        else:                      return False
    if alt == False:
        check = pieces0[Pindex]
        if check.find(color) == 1 :return False
        else:                      return True

def smartmove(moveboard, Index, dist):
    #Keeps name but marks as "##"
    spaces = moveboard[Index+dist].count(" ")
    Aname = str(moveboard[Index+dist].replace(" ", ""))
    moveboard[Index+dist] = str("#"+ Aname + " "*(spaces-2)+ "#")

def pawn(moveboard, color, Index):
    if color == "w":
        acolor = "b"
        i = 8
    if color == "b":
        acolor = "w"
        i = -8
    if moveboard[Index+i] == "         ":
        moveboard[Index+i] = "#       #"
        if color == "w" and Index < 16 and moveboard[Index+16] == "         ":
            moveboard[Index+16] = "#       #"
        if color == "b" and Index > 47 and moveboard[Index-16]:
            moveboard[Index-16] = "#       #"
    if Index % 8 != 7 and moveboard[Index+i+1].find(acolor, 0, 2) == 1:
        smartmove(moveboard, Index, i+1)
    if Index % 8 != 0 and moveboard[Index+i-1].find(acolor, 0, 2) == 1:
        smartmove(moveboard, Index, i-1)

def king(moveboard, color, Index):
            
    #Up
    if Index > 7:            
        #Left
        if Index % 8 != 0 and moveboard[Index-9].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, -9)
        #Mid
        if moveboard[Index-8].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, -8)
        #Right
        if Index % 8 != 7 and moveboard[Index-7].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, -7)
    #Left 
    if Index % 8 != 0 and moveboard[Index-1].find(color, 0, 2) == -1:
        smartmove(moveboard, Index, -1)
    #Right
    if Index % 8 != 7 and moveboard[Index+1].find(color, 0, 2) == -1:
        smartmove(moveboard, Index, +1)
    #Down
    if Index < 56:
        #Right
        if Index % 8 != 7 and moveboard[Index+9].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, 9)
        #Mid
        if moveboard[Index+8].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, 8) 
        #Left
        if Index % 8 != 0 and moveboard[Index+7].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, 7)

def knight(moveboard, color, Index):
    #UP VERT
    if Index > 14 and Index % 8 != 0:
        if moveboard[Index-15].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, -15)
    if Index > 15 and Index % 8 != 7:
        if moveboard[Index-17].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, -17)
    #UP HOR
    if Index > 9 and Index % 8 > 1:
        if moveboard[Index-10].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, -10)
    if Index > 7 and Index % 8 < 6:
        if moveboard[Index-6].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, -6)
    #DOWN HOR
    if Index < 57 and Index % 8 > 1:
        if moveboard[Index+6].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, 6)
    if Index < 55 and Index % 8 < 6:
        if moveboard[Index+10].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, 10)
    #DOWN VERT
    if Index < 48 and Index % 8 != 0:
        if moveboard[Index+15].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, 15)
    if Index < 47 and Index % 8 != 7:
        if moveboard[Index+17].find(color, 0, 2) == -1:
            smartmove(moveboard, Index, 17)

def rook(moveboard, color, Index):
    if color == "w": acolor = "b"
    if color == "b": acolor = "w"
    leftspace  = Index % 8
    rightspace = 7 - leftspace
    upspace    = Index // 8
    downspace  = 7 - upspace
    i = 1
    
    #HOR LEFT
    while i <= leftspace:
        if moveboard[Index-i] == "         ":
            moveboard[Index-i] = "#       #"
        if moveboard[Index-i].find(acolor, 0, 2) == 1:
            smartmove(moveboard, Index, -i)
            i += 10
        if moveboard[Index-i].find(color, 0, 2) == 1:
            i += 10
        i += 1
    i = 1
    #HOR RIGHT
    while i <= rightspace:
        if moveboard[Index+i] == "         ":
            moveboard[Index+i] = "#       #"
        if moveboard[Index+i].find(acolor, 0, 2) == 1:   
            smartmove(moveboard, Index, i)
            i += 10
        if moveboard[Index+i].find(color, 0, 2) == 1:
            i += 10            
        i += 1
    i = 1
    #VERT UP
    while i <= upspace:
        n = 8*i
        if moveboard[Index-n] == "         ":
            moveboard[Index-n] = "#       #"
        if moveboard[Index-n].find(acolor, 0, 2) == 1:
            smartmove(moveboard, Index, -n)
            i += 10
        if moveboard[Index-n].find(color, 0, 2) == 1:
            i += 10
        i += 1
    i = 1
    #VERT DOWN
    while i <= downspace:
        n = 8*i
        if moveboard[Index+n] == "         ":
            moveboard[Index+n] = "#       #"
        if moveboard[Index+n].find(acolor, 0, 2) == 1:
            smartmove(moveboard, Index, n)
            i += 10
        if moveboard[Index+n].find(color, 0, 2) == 1:
            i += 10
        i += 1
    i = 1
    
def bishop(moveboard, color, Index):
    if color == "w": acolor = "b"
    if color == "b": acolor = "w"
    
    leftspace  = Index % 8
    rightspace = 7 - leftspace
    upspace    = Index // 8
    downspace  = 7 - upspace
    i = 1             
    #Upleft
    while i <= leftspace and i <= upspace:
        n = 8*i + i
        if moveboard[Index-n].find(acolor, 0, 2) == 1:
            smartmove(moveboard, Index, -n)
            i += 10                    
        if moveboard[Index-n].find(color, 0, 2) == -1 and i <= leftspace and i <= upspace:
            smartmove(moveboard, Index, -n)
        if moveboard[Index-n].find(color, 0, 2) == 1:
            i += 10
        i += 1
    i = 1
    #Upright
    while i <= rightspace and i <= upspace:
        n = 8*i - i
        if moveboard[Index-n].find(acolor, 0, 2) == 1:
            smartmove(moveboard, Index, -n)
            i += 10
        if moveboard[Index-n].find(color, 0, 2) == -1 and i <= rightspace and i <= upspace:
            smartmove(moveboard, Index, -n)
        if moveboard[Index-n].find(color, 0, 2) == 1:
            i += 10
        i += 1
    i = 1
    #Downleft
    while i <= leftspace and i <= downspace:
        n = 8*i - i
        if moveboard[Index+n].find(acolor, 0, 2) == 1:
            smartmove(moveboard, Index, +n)
            i += 10
        if moveboard[Index+n].find(color, 0, 2) == -1 and i <= leftspace and i <= downspace:
            smartmove(moveboard, Index, +n)
        if moveboard[Index+n].find(color, 0, 2) == 1:
            i += 10
        i += 1
    i = 1
    #Downright
    while i <= rightspace and i <= downspace:
        n = 8*i + i
        if moveboard[Index+n].find(acolor, 0, 2) == 1:
            smartmove(moveboard, Index, +n)
            i += 10
        if moveboard[Index+n].find(color, 0, 2) == -1 and i <= rightspace and i <= downspace:
            smartmove(moveboard, Index, +n)
        if moveboard[Index+n].find(color, 0, 2) == 1:
            i += 10
        i += 1

def promocheck(Index, color):
    if color == "w" and Index > 55 or color == "b" and Index < 8:
        lst = [" "+ color +"Queen  ", " "+ color +"Bishop ", " "+ color+ "Knight ", " "+ color +"Rook   "]
        lst2 = ["1", "2", "3", "4"]
        x = "0"
        x = input("Promotion available: Queen(1), Bishop(2), Knight(3), Rook(4): ")
        if x not in lst2 or x.isalnum == False:
            x = input("False input. Pick a number from 1-4: ")
        if x in lst2: return(lst[int(x)-1])
    return(" "+ color +"Pawn   ")

def castle(moveboard, color, Index):
    if color == "w" and Index == 4 and hasmoved["4"] == False:
        LoSr = False
        LoSl = False
        
        if hasmoved["0"] == False: LoSr = LoS(moveboard, color, Index, "r")
        if hasmoved["7"] == False: LoSl = LoS(moveboard, color, Index, "l")
        if LoSr == True: moveboard[2] = "*       *"
        if LoSl == True: moveboard[6] = "*       *"
        
    if color == "b" and Index == 60 and hasmoved["60"] == False:
        if hasmoved["56"] == False: LoSr = LoS(moveboard, color, Index, "r")
        else: LoSr = False
        if hasmoved["63"] == False: LoSl = LoS(moveboard, color, Index, "l")
        else: LoSl = False
        if LoSr == True: moveboard[58] = "*       *"
        if LoSl == True: moveboard[62] = "*       *" 
        
def LoS(moveboard, color, Index, dir):
    if color == "w": acolor = "b"
    if color == "b": acolor = "w"
    leftspace  = Index % 8
    rightspace = 7 - leftspace
    i = 0
    #HOR LEFT
    while i <= leftspace and dir == "l":
        if moveboard[Index-i].find(acolor, 0, 2) == 1:
            smartmove(moveboard, Index, -i)
            i += 10
        if moveboard[Index-i].find(color + "King") == 1:
            return(True)      
        if moveboard[Index-i].find(color, 0, 2) == 1:
            i += 10
        i += 1
    #HOR RIGHT
    while i <= rightspace and dir == "r":
        if moveboard[Index+i].find(acolor, 0, 2) == 1:   
            smartmove(moveboard, Index, i)
            i += 10
        if moveboard[Index+i].find(color + "King") == 1:
            return(True)
        if moveboard[Index+i].find(color, 0, 2) == 1:
            i += 10            
        i += 1
    return(False)

def initmove(type, color, Index):
    if type == "wKing": hasmoved["4"]  = True
    if type == "bKing": hasmoved["60"] = True
    
    if type == "wRook":
        if Index == 0: hasmoved["0"] =                 True
        if Index == 7: hasmoved["7"] =                 True
    if type == "bRook":
        if Index == 56: hasmoved["56"] =               True
        if Index == 63: hasmoved["63"] =               True
"""
    if type == "pawn":
        if color == "w":
            if Index 
        if color == "b":
"""
def moveboard(Index, pieces0, color):
    slotname = pieces0[Index]
    type     = pieces0[Index]
    type = type.replace(" ", "")
    #At this point, you'll get sth like "bRook"
    moveboard = pieces0.copy()
        
    if type.startswith("w") == True:
        
        if type == "wPawn":
            pawn(moveboard, "w", Index)
    
        if type == "wKing":
            king(moveboard, "w", Index)
            castle(moveboard, color, Index)
            initmove(type, "w", Index)
            
        if type == "wKnight":
            knight(moveboard, color, Index)
        
        if type == "wRook":
            rook(moveboard, color, Index)
            initmove(type, color, Index)
            
        if type == "wBishop":
            bishop(moveboard, color, Index)

        if type == "wQueen":
            rook(moveboard, color, Index)
            bishop(moveboard, color, Index)
    
    if type.startswith("b") == True:

        if type == "bPawn":
            pawn(moveboard, "b", Index)
    
        if type == "bKing":
            king(moveboard, "b", Index)
            castle(moveboard, color, Index)
            initmove(type, color, Index)
 
        if type == "bKnight":
            knight(moveboard, "b", Index)
    
        if type == "bRook":
            rook(moveboard, color, Index)
            initmove(type, color, Index)        
   
        if type == "bBishop":
            bishop(moveboard, color, Index)
    
        if type == "bQueen":
            rook(moveboard, color, Index)
            bishop(moveboard, color, Index)

    printboard(moveboard)

    yIndex = coordget1(color, False)
    if yIndex[1] == False or yIndex[0] == "False": return (False)
    if moveboard[yIndex[0]].startswith("#") == 1:
        pieces0[yIndex[0]] = slotname
        pieces0[Index] = "         "
        if pieces0[yIndex[0]] == " "+ color +"Pawn   ":
            pieces0[yIndex[0]] = promocheck(yIndex[0], color)
    if moveboard[yIndex[0]].startswith("*") == 1:
        pieces0[yIndex[0]] = " "+ color +"King   "
        pieces0[Index] = "         "
        if Index - yIndex[0] < 0:
            pieces0[Index+1] = " "+ color +"Rook   "
            pieces0[Index+3] = "         "
        if Index - yIndex[0] > 0:
            pieces0[Index-1] = " "+ color +"Rook   "
            pieces0[Index-4] = "         "
        
    printboard(pieces0)
    if pieces0 != moveboard: return(True)
    else:                    return(False)

printboard(pieces0)

def gameloop():
    over = False
    i = 0
    while over == False:
    
        if i % 2 == 0:
            color = "w"
        else:
            color = "b"
    
        Index = coordget1(color, True)        
        
        if Index[1] == False or Index[0] == False:
            print("Not a valid selection!")
        if Index[1] == True:
            printboard(pieces0)
            x = moveboard(Index[0], pieces0, color)
            if x == True: i += 1

        if " wKing   " not in pieces0:
            print("Player 2 wins!")
            over = True
        if " bKing   " not in pieces0:
            print("Player 1 wins!")
            over = True
        
gameloop()