def sum(a,b,c):
    return a+b+c
def checkwin(x,O):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for win in wins:
        if(sum(x[win[0]],x[win[1]],x[win[2]]) == 3):
            print(" X win")
            return 1
        if(sum(O[win[0]],O[win[1]],O[win[2]]) == 3):
            print(" O win")
            return 0 
             
    return -1


def printchart(x,O):
    zero='X' if x[0] else ('O' if O[0] else 0)
    one='X' if x[1] else ('O' if O[1] else 1)
    Two='X' if x[2] else ('O' if O[2] else 2)
    Three='X' if x[3] else ('O' if O[3] else 3)
    Four='X' if x[4] else ('O' if O[4] else 4)
    Five='X' if x[5] else ('O' if O[5] else 5)
    Six='X' if x[6] else ('O' if O[6] else 6)
    Seven='X' if x[7] else ('O' if O[7] else 7)
    Eight='X' if x[8] else ('O' if O[8] else 8)

    print(f" {zero} | {one} | {Two}")         # f - string used
    print("---|---|---")
    print(f" {Three} | {Four} | {Five}")        # f - string used
    print("---|---|---")
    print(f" {Six} | {Seven} | {Eight}")        # f - string used
    
print("Welcome to TicTacToe")
x=[0,0,0,0,0,0,0,0,0]
O=[0,0,0,0,0,0,0,0,0]
chance=1
count=0
while True:
    if(chance==1):
        printchart(x,O)
        print(" X Chance")
        i=int(input("Enter Position Number :"))
        x[i]=1
        chance=-1
        count+=1
    else:
        printchart(x,O)
        print(" 0 Chance")
        i=int(input("Enter Position Number :"))
        O[i]=1
        chance=1
        count+=1
    c=checkwin(x,O)
    if c != -1:
        break
    if count == 9:
        print("Match Draw")
        break

