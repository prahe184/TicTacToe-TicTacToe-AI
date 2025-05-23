import time
import math
import random
from tictactoe import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # we will use a single list to rep 3*3 board
        self.current_winner = None #keep track of winner
     
    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
             print('|' + '|'.join(row) + '|')

    @staticmethod 
    def print_board_nums():
          number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
          for row in number_board:
               print('|' + '|'.join(row) + '|')


         

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot== ' ']
    
    def empty_squares(self):
         return ' ' in self.board
    
    def num_empty_squares(self):
         return self.board.count(' ')
    
    def make_move(self,square,letter):
         if self.board[square] == ' ':
              self.board[square]= letter
              if self.winner(square, letter):  # Update current_winner if there's a winner
                 self.current_winner = letter
              return True
         return False
    
    def winner(self, square, letter ):
         #winner if 3 in a row anywhere... we have to check all of these!
         row_ind = square // 3
         row = self.board[row_ind*3 : (row_ind+1)*3]
         if all ([spot == letter for spot in row]):
              return True
         
         #checks column
         col_ind = square % 3
         column = [self.board[col_ind+i*3] for i in range(3)]
         if all ([spot == letter for spot in column]):
              return True
         
         #check diagonals
         #but only if a square is an even number (0, 2, 4, 6, 8)
         #these are the only moves possible to win a diagnol
         if square % 2 == 0:
               diagnol1 = [self.board[i] for i in [0,4,8]] #left to right diagnol
               if all([spot == letter for spot in diagnol1]):
                   return True
               diagnol2 = [self.board[i] for i in [2,4,6]] #right to left diagnol
               if all([spot == letter for spot in diagnol2]):
                   return True
          #if all these fail    
         return False
    @staticmethod 
    def play(game, x_player, o_player, print_game = True):
           if print_game:
                game.print_board_nums()
          
           letter = 'X' #starting letter
           #iterate while the game still has empty squares
           #(we don't have to worry about the winner because we'll just return that
           #which breaks the loop)
           while game.empty_squares():
               if letter == "O":
                    square = o_player.get_move(game)
               else:
                     square = x_player.get_move(game)
                
               if game.make_move(square,letter):
                     if print_game:
                         print(letter + f"makes a move to square {square}")
                         game.print_board()
                         print(' ') #just empty line
                     if game.winner(square, letter):
                           game.current_winner=letter
                           if print_game:
                                 print(letter +'wins' )
                           return letter
                     #after we made our move we need to alternate letters
                     letter = 'O' if letter == 'X' else 'X' #switches player

               time.sleep(0.8)

           if print_game:
                     print("It's a tie")

if __name__ == '__main__':
     x_player = HumanPlayer('X')
     o_player = GeniusComputerPlayer('O')
     t = TicTacToe()
     TicTacToe.play(t , x_player, o_player, print_game=True)

                          

                

    
