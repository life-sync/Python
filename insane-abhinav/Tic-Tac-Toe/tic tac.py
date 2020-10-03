#initialization
x_count = 0
o_count = 0
s_count = 0
game_still_on = True
current_player = "X"
#initializing list to empty( _ )
list = ["_" ,"_" ,"_" ,"_" ,"_" ,"_" ,"_" ,"_" ,"_" ]
#function defination
def display(): #function to display the matrix
  print("-------------------")
  print("|  "+list[0]+"  |  "+list[1]+"  |  "+list[2]+"  |")
  print("|  "+list[3]+"  |  "+list[4]+"  |  "+list[5]+"  |")
  print("|  "+list[6]+"  |  "+list[7]+"  |  "+list[8]+"  |")
  print("-------------------")
def count(): #function to count the number of X ,O and _ in the list
  global x_count,o_count,s_count
  x_count = o_count = s_count = 0
  for x in list:
    if x == "X":
        x_count = x_count + 1
    elif x == "O":
        o_count = o_count + 1
    elif x == "_":
        s_count = s_count + 1

def check(): #function to check the winner
  global game_still_on
  if ((list[0] == list[1] == list[2] == "X" or list[3] == list[4] == list[5] == "X" or list[6] == list[7] == list[8] == "X" or list[0] == list[3] == list[6] == "X" or list[1] == list[4] == list[7] == "X" or list[2] == list[5] == list[8] == "X" or list[0] == list[4] == list[8] == "X" or list[2] == list[4] == list[6] == "X") and (list[0] == list[1] == list[2] == "O" or list[3] == list[4] == list[5] == "O" or list[6] == list[7] == list[8] == "O" or list[0] == list[3] == list[6] == "O" or list[1] == list[4] == list[7] == "O" or list[2] == list[5] == list[8] == "O" or list[0] == list[4] == list[8] == "O" or list[2] == list[4] == list[6] == "O")) or ((x_count-o_count) >= 2 or (o_count-x_count) >= 2):
    print("Impossible")
    game_still_on = False
  elif list[0] == list[1] == list[2] == "X" or list[3] == list[4] == list[5] == "X" or list[6] == list[7] == list[8] == "X" or list[0] == list[3] == list[6] == "X" or list[1] == list[4] == list[7] == "X" or list[2] == list[5] == list[8] == "X" or list[0] == list[4] == list[8] == "X" or list[2] == list[4] == list[6] == "X":
    print("X wins")
    game_still_on = False
  elif list[0] == list[1] == list[2] == "O" or list[3] == list[4] == list[5] == "O" or list[6] == list[7] == list[8] == "O" or list[0] == list[3] == list[6] == "O" or list[1] == list[4] == list[7] == "O" or list[2] == list[5] == list[8] == "O" or list[0] == list[4] == list[8] == "O" or list[2] == list[4] == list[6] == "O":
    print("O wins")
    game_still_on = False
  else:
    if s_count == 0:
      print("Draw")
      game_still_on = False
def get_input(current_player): #function to take the index input
  print()
  print("------"+current_player+"'s turn! ------")
  index = input("Enter the index (1-9) : ")
  if index in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]: #checking whether input lies between 1-9
    index = int(index) - 1
    if list[index] != "_" : #checking whether the index is empty
      print("Index is already occupied!!!")
      get_input(current_player)
    else :
      list[index] = current_player
  else:
    print("Invalid Input!!!!")
    get_input(current_player)
def switch_player(): #function to switch the player
  global current_player
  if current_player == "X": #if the current player is X then switch to O
    current_player = "O"
  elif current_player == "O": #if the current player is O then switch to X
    current_player = "X"
def play_game(): #function which run the game
  display()
  while game_still_on:
    get_input(current_player)
    display()
    count()
    check()
    switch_player()
#function call
play_game()
