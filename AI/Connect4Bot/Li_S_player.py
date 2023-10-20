# Name: Steven Li
# Date: 12/18/2020
import random
class RandomPlayer:
   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 7
      self.y_max = 6
      self.first_turn = True
      
   def best_strategy(self, board, color):
      # returns best move
      # (column num, row num), 0
      l=list(self.find_moves(board,color))
      move=random.choice(l)
      return [move//self.y_max,move%self.y_max],0
      
     
   def find_moves(self, my_board, color):
      moves=[]
      for i in range(len(my_board)):
         c=-1
         while my_board[i][c+1]==".":
            c=c+1
            if c==self.y_max-1: break
         if c!=-1: moves.append(i*self.y_max+c)
      #print(moves)
      return moves

class Best_AI_bot:

   def __init__(self):
      self.white = "O"
      self.black = "@"
      self.opposite_color = {self.black: self.white, self.white: self.black}
      self.x_max = 7
      self.y_max = 6
      self.first_turn = True
      self.table=self.static_table()
   def best_strategy(self, board, color):
      # if len(self.find_moves(board,color))>23:
      #    if board[2][2]=='.': 
      #       return [2,2],0
      self.x_max = len(board)
      self.y_max = len(board[0])
      if color == "#000000":
         color = "@"
      else:
         color = "O"
      #self.first_turn=self.first_turn+1
      return self.minimax(board,color,4)

   def minimax(self, board, color, search_depth):
      possible=self.find_moves(board,color)
      max=float('-inf')
      best_move=None
      for move in possible:
         b=self.make_move(board,color,move)
         score=self.minV(b,self.opposite_color[color],search_depth)
         if score>max:
            max=score
            best_move=move
      return [best_move//self.y_max,best_move%self.y_max], max
   def maxV(self,board,color,search_depth):
      # if len(self.find_moves(board,color))==0:
      #    print("false")
      #    return -1 
      # if search_depth>=8:
      #    print(search_depth)
      #    return self.evaluate(board,color,self.find_moves(board,color))
      # scores=[]
      # for move in self.find_moves(board,color):
      #    print(move)
      #    scores.append(self.minV(self.make_move(board,color,move),self.opposite_color[color],search_depth+1))
      # print(scores)
      # return max(scores)
      possible=self.find_moves(board,color)
      if len(possible)==0: return 0
      if self.win_state(board,color): return 10000
      if self.win_state(board,self.opposite_color[color]): return -10000
      if search_depth==1: return self.evaluate(board,color)
      max=float('-inf')
      for move in possible:
         b=self.make_move(board,color,move)
         v=self.minV(b,self.opposite_color[color],search_depth-1)
         if v>max:
            max=v
      return max
   def minV(self,board,color,search_depth):
      # if len(self.find_moves(board,color))==0:
      #    print("false")
      #    return 1
      # if search_depth>=8:
      #    print(search_depth)
      #    return self.evaluate(board,color,self.find_moves(board,color))
      # scores=[]
      # for move in self.find_moves(board,color):
      #    scores.append(self.maxV(self.make_move(board,color,move),self.opposite_color[color],search_depth+1))
      # print(scores)
      # return min(scores)
      possible=self.find_moves(board,color)
      if len(possible)==0: return 0
      if self.win_state(board,color): return -10000
      if self.win_state(board,self.opposite_color[color]): return 10000
      if search_depth==1: return self.evaluate(board,color)*-1
      min=float('inf')
      for move in possible:
         b=self.make_move(board,color,move)
         v=self.maxV(b,self.opposite_color[color],search_depth-1)
         if v<min:
            min=v
      return min


   def win_state(self,board,piece):
      for c in range(self.y_max-3):
         for r in range(self.x_max):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
               return True

      # Check vertical locations for win
      for c in range(self.y_max):
         for r in range(self.x_max-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
               return True

      # Check positively sloped diaganols
      for c in range(self.y_max-3):
         for r in range(self.x_max-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
               return True

      # Check negatively sloped diaganols
      for c in range(self.y_max-3):
         for r in range(3, self.x_max):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
               return True
      return False
   def make_move(self, board, color, move):
      # returns board that has been updated
      board2=[[x for x in row] for row in board]
      move0=move//self.y_max
      move1=move%self.y_max
      board2[move0][move1]=color
      return board2

   def evaluate(self, board, color):
      count1=0
      count2=0
      for i in range(len(board)):
         for j in range(len(board[i])):
            if board[i][j]==color:
               count1=count1+self.table[i][j]
            elif board[i][j]==self.opposite_color[color]:
               count2=count2+self.table[i][j]
      return 138+count1-count2
   def find_moves(self, my_board, color):
      moves=[]
      for i in range(len(my_board)):
         c=-1
         while my_board[i][c+1]==".":
            c=c+1
            if c==self.y_max-1: break
         if c!=-1: moves.append(i*self.y_max+c)
      return moves
   def static_table(self):
      return [[3,4,5,5,4,3],[4,6,8,8,6,4],[5,8,11,11,8,5],[7,10,13,13,10,7],[5,8,11,11,8,5],[4,6,8,8,6,4],[3,4,5,5,4,3]]
