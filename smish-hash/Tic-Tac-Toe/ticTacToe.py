# WAP to create a 2 player tic tac toe nextGame
#Implementation of Two Player Tic-Tac-Toe nextGame in Python.

Game = {'1': ' ' , '2': ' ' , '3': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '7': ' ' , '8': ' ' , '9': ' ' }

key_list = []

for key in Game:
    key_list.append(key)

player1 = input("Player 1: ")
player2 = input("Player 2: ")
print("\n%s => X\n%s => O\n" %(player1, player2))
print("Layout:")
print('1' + '|' + '2' + '|' + '3')
print('-+-+-')
print('4' + '|' + '5' + '|' + '6')
print('-+-+-')
print('7' + '|' + '8' + '|' + '9')
print("\nGame begins!")

def printGame(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def nextGame():
    ch = 'X'
    player = player1
    count = 0

    for i in range(10):
        printGame(Game)
        print("%s's turn. Select position to mark:" %(player))

        move = input()

        if Game[move] == ' ':
            Game[move] = ch
            count += 1
        else:
            print("Invalid  move!.\nPlease try again")
            continue

        if count >= 5:
            if Game['7'] == Game['8'] == Game['9'] != ' ':
                printGame(Game)
                print("\nGame Over.\n")
                print("%s is the winner!!" %(player))
                break
            elif Game['4'] == Game['5'] == Game['6'] != ' ':
                printGame(Game)
                print("\nGame Over.\n")
                print("%s is the winner!!" %(player))
                break
            elif Game['1'] == Game['2'] == Game['3'] != ' ':
                printGame(Game)
                print("\nGame Over.\n")
                print("%s is the winner!!" %(player))
                break
            elif Game['1'] == Game['4'] == Game['7'] != ' ':
                printGame(Game)
                print("\nGame Over.\n")
                print("%s is the winner!!" %(player))
                break
            elif Game['2'] == Game['5'] == Game['8'] != ' ':
                printGame(Game)
                print("\nGame Over.\n")
                print("%s is the winner!!" %(player))
                break
            elif Game['3'] == Game['6'] == Game['9'] != ' ':
                printGame(Game)
                print("\nGame Over.\n")
                print("%s is the winner!!" %(player))
                break
            elif Game['7'] == Game['5'] == Game['3'] != ' ':
                printGame(Game)
                print("\nGame Over.\n")
                print("%s is the winner!!" %(player))
                break
            elif Game['1'] == Game['5'] == Game['9'] != ' ':
                printGame(Game)
                print("\nGame Over.\n")
                print("%s is the winner!!" %(player))
                break

        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        if ch =='X':
            ch = 'O'
            player = player2
        else:
            ch = 'X'
            player = player1

    replay = input("Do you wish to play Again?(y/n)")
    if replay == "y" or replay == "Y":
        for key in key_list:
            Game[key] = " "

        nextGame()

if __name__ == "__main__":
    nextGame()
