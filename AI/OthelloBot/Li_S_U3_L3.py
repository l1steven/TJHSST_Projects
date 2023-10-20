# Name:Steven Li
# Date:1/15/2021

import random

class RandomBot:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 8
      self.y_max = 8

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      ''' Your code goes here ''' 
      l=list(self.find_moves(board,color).keys())
      move=random.choice(l)
      return [move//self.x_max,move%self.y_max],0

   def stones_left(self, my_board):
      # returns number of stones that can still be placed (empty spots)
      count=0
      for i in range(len(my_board)):
         for j in range(len(my_board[i])):
            if my_board[i][j]==".":
               count=count+1

   def find_moves(self, my_board, my_color):
    # finds all possible moves
      moves_found = {}
      for i in range(len(my_board)):
        for j in range(len(my_board[i])):
            flipped_stones = self.find_flipped(my_board, i, j, my_color)
            if len(flipped_stones) > 0:
                moves_found.update({i*self.y_max+j: flipped_stones})
      return moves_found


   def find_flipped(self, my_board, x, y, my_color):
    # finds which chips would be flipped given a move and color
      if my_board[x][y] != ".":
        return []
      if my_color == self.black:
        my_color = "@"
      else:
        my_color = "O"
      flipped_stones = []
      for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if my_board[x_pos][y_pos] == ".":
                break
            if my_board[x_pos][y_pos] == my_color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
      return flipped_stones

class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 8
      self.y_max = 8
      self.table=self.static_table()

   def best_strategy(self, board, color):
      # returns best move
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      
      possible=self.find_moves(board,color)
      if 0 in possible: return [0,0],0
      elif 7 in possible: return [0,7],0
      elif 56 in possible: return [7,0],0
      elif 63 in possible: return [7,7],0
      # for move in possible:
      #    b=self.make_move(board,color,move,possible[move])
      #    if len(self.find_moves(b,self.opposite_color[color]))==0:
      #       return [move//self.x_max,move%self.y_max],0
      return self.minimax(board,color,4)


   def minimax(self, board, color, search_depth):
      possible=self.find_moves(board,color)
      max=float('-inf')
      best_move=None
      for move in possible:
         b=self.make_move(board,color,move,possible[move])
         score=self.minV(b,self.opposite_color[color],search_depth)
         #score=self.negamax(b,self.opposite_color[color],6)
         if score>max:
            max=score
            best_move=move
      #self.first_turn=self.first_turn+1
      return [best_move//self.x_max,best_move%self.y_max], max
   def maxV(self,board,color,search_depth):
      possible=self.find_moves(board,color)
      if len(possible)==0: return -10000
      if len(self.find_moves(board,self.opposite_color[color]))==0: return 10000
      if search_depth==1: return self.evaluate(board,color,possible)
      max=float('-inf')
      for move in possible:
         b=self.make_move(board,color,move,possible[move])
         v=self.minV(b,self.opposite_color[color],search_depth-1)
         if v>max:
            max=v
      return max
   def minV(self,board,color,search_depth):
      possible=self.find_moves(board,color)
      if len(possible)==0: return 10000
      elif len(self.find_moves(board,self.opposite_color[color]))==0: return -10000
      if search_depth==1: return self.evaluate(board,color,possible)*-1
      min=float('inf')
      for move in possible:
         b=self.make_move(board,color,move,possible[move])
         v=self.maxV(b,self.opposite_color[color],search_depth-1)
         if v<min:
            min=v
      return min
      

   def negamax(self, board, color, search_depth):
    # returns best "value"
      return 1
      
   def alphabeta(self, board, color, search_depth, alpha, beta):
    # returns best "value" while also pruning
      pass

   def make_key(self, board, color):
    # hashes the board
      return 1

   def stones_left(self, my_board):
    # returns number of stones that can still be placed
      count=0
      for i in range(len(my_board)):
         for j in range(len(my_board[i])):
            if my_board[i][j]==".":
               count=count+1
   def static_table(self):
      return [[4,-3,2,2,2,2,-3,4],[-3,-4,-1,-1,-1,-1,-4,-3],[2,-1,1,0,0,1,-1,2],[2,-1,0,1,1,0,-1,2],[2,-1,0,1,1,0,-1,2],[2,-1,1,0,0,1,-1,2],[-3,-4,-1,-1,-1,-1,-4,-3],[4,-3,2,2,2,2,-3,4]]
   def make_move(self, board, color, move, flipped):
      # returns board that has been updated
      board2=[[x for x in row] for row in board]
      move0=move//self.x_max
      move1=move%self.y_max
      board2[move0][move1]=color
      for flip in flipped:
         board2[flip[0]][flip[1]]=color
      return board2

   def evaluate(self, board, color, possible_moves):
      # returns the utility value
      count1=0
      count2=0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j]==color:
               count1=count1+self.table[i][j]
            elif board[i][j]==self.opposite_color[color]:
               count2=count2+self.table[i][j]
      return count1-count2
      

   def score(self, board, color):
      # returns the score of the board 
      score1=0
      score2=0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j] == "@":
                score1 += 1
            if board[i][j] == "O":
                score2 += 1
      return score1,score2

   def find_moves(self, my_board, my_color):
    # finds all possible moves
      moves_found = {}
      for i in range(len(my_board)):
        for j in range(len(my_board[i])):
            flipped_stones = self.find_flipped(my_board, i, j, my_color)
            if len(flipped_stones) > 0:
                moves_found.update({i*self.y_max+j: flipped_stones})
      return moves_found

   def find_flipped(self, my_board, x, y, my_color):
    # finds which chips would be flipped given a move and color
      if my_board[x][y] != ".":
        return []
      if my_color == self.black:
        my_color = "@"
      else:
        my_color = "O"
      flipped_stones = []
      for incr in self.directions:
        temp_flip = []
        x_pos = x + incr[0]
        y_pos = y + incr[1]
        while 0 <= x_pos < self.x_max and 0 <= y_pos < self.y_max:
            if my_board[x_pos][y_pos] == ".":
                break
            if my_board[x_pos][y_pos] == my_color:
                flipped_stones += temp_flip
                break
            temp_flip.append([x_pos, y_pos])
            x_pos += incr[0]
            y_pos += incr[1]
      return flipped_stones