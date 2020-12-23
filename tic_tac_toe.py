"""Tik Tak Toe"""
import random
def display_board(board):
     # This function Display the box format for the game
     print('-------------')
     print('| '+board[1]+ ' | '+board[2]+' | '+board[3]+' |')
     print('-------------')
     print('| '+board[4]+ ' | '+board[5]+' | '+board[6]+' |')
     print('-------------')
     print('| '+board[7]+ ' | '+board[8]+' | '+board[9]+' |')
     print('-------------')


def player_marker():
     #Assign a marker to a variable ie) X or O
     marker=' '
     while not (marker=='X' or marker=='O'):
          marker=input('Player 1: Enter your choice X or O: ').upper()
          if marker=='X':
               return ('X','O')
          elif marker=='O':
               return ('O','X')
          else:
               print('Sorry! Enter the correct choice!!')

def place_maker(board,marker,position):
     #get the position and assign to the desire marker
     board[position]=marker 
     return board

def random_check():
     # Returns the random between Playe 1 and Player 2
     num=random.randint(0,1)
     if num==0:
          return 'Player 1'
     else:
          return 'Player 2'

def win_game(board,marker):
     # Checks who os the winner of the game
     return (board[1]==board[2]==board[3]==marker or 
     board[4]==board[5]==board[6]==marker or 
     board[7]==board[8]==board[9]==marker or 
     board[1]==board[4]==board[7]==marker or
     board[2]==board[5]==board[8]==marker or
     board[3]==board[6]==board[9]==marker or
     board[1]==board[5]==board[9]==marker or
     board[3]==board[5]==board[7]==marker)

def space_check(board,position):
     # Checks that whether space is available in the desire position
     return board[position]==' '

def if_full(board):
     # cHecks whether the board is full
     ## It will use to check whether the game is tie or not
     for i in range(1,10):
          if board[i]==' ':
               #Space available
               return False
     return True

def player_choice(board):
     # Gets the position from the player to place the marker
     position = ''
     while position not in ['1','2','3','4','5','6','7','8','9'] or not space_check(board, int(position)) or not position.isdigit() :
         position = input('Choose your next position: (1-9) ')
         if not space_check(board,int(position)):
              print('This position is occupied, enter a correct position!!!')
         if not position.isdigit()==True:
              print('Please enter values between (1-9)')
     return int(position)

def reply():
     reply=' '
     while not (reply=='Y' or reply=='N'):
          reply=input('Do you want to play again? Enter Y or N: ').upper()
          if reply=='Y':
               return True
          elif reply=='N':
               return False
          else:
               print("Sorry,Enter a correct choice!!")


print('Welcome to TIC TAK TOE!!!')
while True:
     # 1. Define the board
     the_board=[' ']*10
     # 2. Get the player marker
     player1_marker,player2_marker=player_marker()
     # 3. Get the turn
     turn=random_check()
     print(turn+' will go first')
     game_play=input("Are you ready to play: Y or N -> ").upper()
     if game_play=='Y':
          game_on=True
     elif game_play=='N':
          game_on=False
     # 4. Play the game
     while game_on:
          if turn=='Player 1':
               display_board(the_board)
               position=player_choice(the_board)
               place_maker(the_board,player1_marker,position)
               if win_game(the_board,player1_marker):
                    display_board(the_board)
                    print('Player 1 won the game')
                    game_on=False
               else:
                    if if_full(the_board):
                         display_board(the_board)
                         print('The game is tie!!')
                         break
                    else:
                         turn='Player 2'
          else:
               display_board(the_board)
               position=player_choice(the_board)
               place_maker(the_board,player2_marker,position)
               if win_game(the_board,player2_marker):
                    display_board(the_board)
                    print('Player 2 won the game')
                    game_on=False
               else:
                    if if_full(the_board):
                         display_board(the_board)
                         print('The game is tie!!')
                         break
                    else:
                         turn='Player 1'
     if reply()==True:
          pass
     else:
          break
     