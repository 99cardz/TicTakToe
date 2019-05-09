

referencefield=[[" "," "," "],
                [" "," "," "],
                [" "," "," "]]
printfield=    [[" "," "," "],
                [" "," "," "],
                [" "," "," "]]
#print(referencefield)

def displayfield():
    for i in range(0,3):
        print(" --- --- --- ")
        print("!", printfield[i][0],"!", printfield[i][1],"!", printfield[i][2],"!")
    print(" --- --- --- ")

def endgame(p):
    print("The winner is Player ",p)


def check(p):
    for i in range(0,3):
        if referencefield[i][0]==p and referencefield[i][1]==p and referencefield[i][2]==p:
            endgame(p)
            return
        if referencefield[0][i]==p and referencefield[1][i]==p and referencefield[2][i]==p:
            endgame(p)
            return
    if referencefield[0][0]==p and referencefield[1][1]==p and referencefield[3][3]==p:
        endgame(p)
        return
    if referencefield[0][2]==p and referencefield[1][1]==p and referencefield[2][0]==p:
        endgame(p)
        return
#Main:

print("Lets start the game")
displayfield()
player=1
while 1:
    try:
        print("Player ", player)
        x=int(input("x:"))
        y=int(input("y:"))
        #print(*referencefield)
        if player == 1 and referencefield[y-1][x-1] == " ":
            referencefield[y-1][x-1] = 1
            printfield[y-1][x-1] = "X"
            check(player)
            player = 2
        elif player == 2 and referencefield[y-1][x-1] == " ":
            referencefield[y-1][x-1] = 2
            printfield[y-1][x-1] = "O"
            check(player)
            player = 1
        else:
            print("this field is already taken")

    except:
        print("please enter a number between 1 and 3!")
    displayfield()
