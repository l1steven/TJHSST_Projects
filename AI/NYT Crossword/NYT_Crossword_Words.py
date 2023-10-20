import sys; args=sys.argv[1:]
import os
import re
import random
import math
#import numpy as np
#Steven Li
#2/28/2021
#python c:\Users\steve\Documents\TJ\AI\assignments\Li_S_U4_L4.py 7x7 0 scrabble.txt V0x0come v0x1here h0x2ERS
# import sys
# import re
# import os
BLOCKCHAR='#'
OPENCHAR='-'
PROTECTEDCHAR='~'
OPPOSITE_DIRECTION={"V":"H","H":"V"}
puzzle=[[]]
rows=0
columns=0
numblocks=0
word_dict={}
word_list=[]
start_dict={}
start_list=[]
def placeword(word,x,y,direction):
   global puzzle
   #print(puzzle)
   for letter in word:
      puzzle[x][y]=letter
      #print(letter)
      if direction=="H": y=y+1
      else: x=x+1
def input():
   global puzzle,rows,columns,numblocks, word_dict, word_list
   filename=""
   intTest = [r"^(\d+)x(\d+)$", r"^\d+$", r"^(H|V)(\d+)x(\d+)(.*)$"]
   for arg in args:
      for i in range(3):
         if os.path.isfile(arg): 
            filename=arg
            print(filename)
            break
         match=re.search(intTest[i],arg,re.I)
         if match:
            if i==0:
               rows=int(match.group(2))
               columns=int(match.group(1))
               #print(rows)
               #print(columns)
               puzzle=[[OPENCHAR for i in range(rows)] for j in range(columns)]
               #print(puzzle)
            elif i==1:
               numblocks=int(match.group())
            else:
               direction=match.group(1).upper()
               x=int(match.group(2))
               y=int(match.group(3))
               #print(y)
               word=match.group(4).upper()
               placeword(word,x,y,direction)
   for i in range(3,max(rows,columns)+1):
      word_dict[i]=[]
   f = open(filename, "r")
   for line2 in f:
      line=line2.replace("\n","")
      if len(line)<=max(rows,columns) and len(line)>=3:
         word_dict[len(line)].append(line.upper())
         word_list.append(line.upper())
   random.shuffle(word_list)
   for i in word_dict:
      random.shuffle(word_dict[i])
def start_positions():
   global start_dict,start_list
   puzzle2=[[x for x in row] for row in puzzle]
   puzzle2.insert(0,[BLOCKCHAR]*rows)
   puzzle2.append([BLOCKCHAR]*rows)
   for row in puzzle2:
      row.insert(0,BLOCKCHAR)
      row.append(BLOCKCHAR)
   for i in range(3,max(rows,columns)+1):
      start_dict[i]=[]
   for i in range(columns+1):
      for j in range(rows+1):
         if puzzle2[i][j]==BLOCKCHAR:
            count=0
            i2=i+1
            while i2<columns+1 and puzzle2[i2][j]!=BLOCKCHAR:
               count=count+1
               i2=i2+1
            if count>=3:
               #start_dict[count].append((i,j-1,"H"))
               if len(puzzle2[i+1][j])==1:
                  puzzle2[i+1][j]="V"+str(count)
               else:
                  puzzle2[i+1][j]=puzzle2[i+1][j]+"?V"+str(count)
            count=0
            j2=j+1
            while j2<rows+1 and puzzle2[i][j2]!=BLOCKCHAR:
               count=count+1
               j2=j2+1
            if count>=3:
               #start_dict[count].append((i-1,j,"V"))
               if len(puzzle2[i][j+1])==1:
                  puzzle2[i][j+1]="H"+str(count)
               else:
                  puzzle2[i][j+1]=puzzle2[i][j+1]+"?H"+str(count)
   puzzle2.pop(columns+1)
   puzzle2.pop(0)
   for row in puzzle2:
      row.pop(rows+1)
      row.pop(0)        
   #display(puzzle2)                   
   for i in range(columns):
      for j in range(rows):
         if len(puzzle2[i][j])>3:
            s=puzzle2[i][j]
            #print(s)
            index=s.index("?")
            direction=s[0]
            count=int(s[1:index])
            start_dict[count].append((i,j,direction))
            direction=s[index+1]
            count=int(s[index+2:])
            start_dict[count].append((i,j,direction))
         elif len(puzzle2[i][j])>1:
            s=puzzle2[i][j]
            direction=s[0]
            count=int(s[1:])
            start_dict[count].append((i,j,direction))
   for i in start_dict:
      start_list=start_list+start_dict[i]
def display(puzzle2):
   for row in puzzle2:
      print(row)


def check3letters(puzzle2):
   check=[(-2,-1,0),(-1,0,1),(0,1,2)]
   bset=set()
   for i in range(columns):
      for j in range(rows):
         if puzzle2[i][j]!=BLOCKCHAR:
            h,v=False,False
            for k in check:
               #try:
                  if i+k[0]>=0 and i+k[1]>=0 and i+k[2]>=0 and i+k[0]<columns and i+k[1]<columns and i+k[2]<columns:
                     if puzzle2[i+k[0]][j]!=BLOCKCHAR and puzzle2[i+k[1]][j]!=BLOCKCHAR and puzzle2[i+k[2]][j]!=BLOCKCHAR:
                        v=True
               #except:
                  #pass
            for k in check:
               #try:
                  if j+k[0]>=0 and j+k[1]>=0 and j+k[2]>=0 and j+k[0]<rows and j+k[1]<rows and j+k[2]<rows:
                     if puzzle2[i][j+k[0]]!=BLOCKCHAR and puzzle2[i][j+k[1]]!=BLOCKCHAR and puzzle2[i][j+k[2]]!=BLOCKCHAR:
                        h=True
               #except:
                  #pass
            bset.add(v and h)
   return False not in bset
def illegal_gaps():
   global puzzle
   puzzle2=[[x for x in row] for row in puzzle]
   puzzle2.insert(0,[BLOCKCHAR]*rows)
   puzzle2.append([BLOCKCHAR]*rows)
   for row in puzzle2:
      row.insert(0,BLOCKCHAR)
      row.append(BLOCKCHAR)
   for i in range(columns+2):
      for j in range(rows+2):
         if puzzle2[i][j]==BLOCKCHAR:
            if i+2<columns and puzzle2[i+2][j]==BLOCKCHAR:
               puzzle2[i+1][j]=BLOCKCHAR
            if i+3<columns and puzzle2[i+3][j]==BLOCKCHAR:
               puzzle2[i+1][j]=BLOCKCHAR
               puzzle2[i+2][j]=BLOCKCHAR
            if j+2<rows and puzzle2[i][j+2]==BLOCKCHAR:
               puzzle2[i][j+1]=BLOCKCHAR
               #print(i,j+1)
               #print(":)")
            if j+3<rows and puzzle2[i][j+3]==BLOCKCHAR:
               puzzle2[i][j+1]=BLOCKCHAR
               puzzle2[i][j+2]=BLOCKCHAR
   puzzle2.pop(columns+1)
   puzzle2.pop(0)
   for row in puzzle2:
      row.pop(rows+1)
      row.pop(0)
   puzzle=[[x for x in row] for row in puzzle2]
def fix180():
   global puzzle
   for i in range(columns):
      for j in range(rows):
         if puzzle[i][j]==BLOCKCHAR:
            puzzle[columns-i-1][rows-j-1]=BLOCKCHAR
def average_word_length(puzzle2):
   sum=0
   total=0
   for i in range(columns):
      inds=[j for j in range(rows) if puzzle2[i][j]==BLOCKCHAR]
      inds.append(-1)
      inds.append(columns)
      inds.sort()
      for z in range(1,len(inds)):
         sum=sum+inds[z]-inds[z-1]-1
         if inds[z]-inds[z-1]-1>0:
            total=total+1
   for j in range(rows):
      inds=[i for i in range(columns) if puzzle2[i][j]==BLOCKCHAR]
      inds.append(-1)
      inds.append(rows)
      inds.sort()
      for z in range(1,len(inds)):
         sum=sum+inds[z]-inds[z-1]-1
         if inds[z]-inds[z-1]-1>0:
            total=total+1
   return sum/total if total!=0 else 0
def possible_blocks():
   middle=(columns-1)//2
   list=[]
   for i in range(middle):
      for j in range(rows):
         if (puzzle[i][j]==OPENCHAR or puzzle[i][j]==PROTECTEDCHAR) and (puzzle[columns-i-1][rows-j-1]==OPENCHAR or puzzle[columns-i-1][rows-j-1]==PROTECTEDCHAR):
         #if puzzle[i][j]==OPENCHAR and puzzle[columns-i-1][rows-j-1]==OPENCHAR:
            move=((i,j),(columns-i-1,rows-j-1))
            #avg=average_word_length(make_move(move[0],move[1]))
            #print(avg)
            #list.append((move,avg))
            list.append(move)
   #ist.sort(key=lambda x: x[1])
   #print(list)
   #newlist=[x[0] for x in list]
   #print(newlist)
   #return newlist
   #return list
   newlist=[]
   for i in list:
      avg=average_word_length(make_move(i[0],i[1]))
      newlist.append((i,avg))
   newlist.sort(key=lambda x:x[1])
   #print(newlist)
   return [p[0] for p in newlist]
def check_complete():
   count=0
   for i in range(columns):
      for j in range(rows):
         if puzzle[i][j]==BLOCKCHAR:
            count=count+1
   return count==numblocks
def checkwalls(puzzle2,x,y):
   if x<0 or x>=columns or y<0 or y>=rows: return 0
   if puzzle2[x][y]==BLOCKCHAR or puzzle2[x][y]=="%": return 0
   puzzle2[x][y]="%"
   return 1+checkwalls(puzzle2,x+1,y)+checkwalls(puzzle2,x-1,y)+checkwalls(puzzle2,x,y+1)+checkwalls(puzzle2,x,y-1)
def findopen2(puzzle2):
   # for i in range(columns):
   #    for j in range(rows):
   #       if puzzle2[i][j]==OPENCHAR or puzzle2[i][j]==PROTECTEDCHAR: return i,j
   # return 0,0
   i=random.randrange(columns)
   j=random.randrange(rows)
   while puzzle[i][j]==BLOCKCHAR:
      i=random.randrange(columns)
      j=random.randrange(rows)
   return i,j
def findopen(puzzle2):
   for i in range(columns):
      for j in range(rows):
         if puzzle2[i][j]==OPENCHAR or puzzle2[i][j]==PROTECTEDCHAR: return i,j
   return 0,0
def walls(puzzle3):
   puzzle2=[[x for x in row] for row in puzzle3]
   x,y=findopen(puzzle2)
   count=0
   for i in range(columns):
      for j in range(rows):
         if puzzle3[i][j]!=BLOCKCHAR: count=count+1
   #print(count)
   #print(checkwalls(puzzle2,x,y))
   #print(checkwalls(puzzle2,x,y)==count)
   return checkwalls(puzzle2,x,y)==count
def wallarea(puzzle2,x,y):
   if x<0 or x>=columns or y<0 or y>=rows: return puzzle2
   if puzzle2[x][y]==BLOCKCHAR or puzzle2[x][y]=="%": return puzzle2
   puzzle2[x][y]=BLOCKCHAR
   # for d in dirs:
   #    if d == -1 and sp % width == 0: continue #left edge
   #    if d == 1 and sp+1 % width == 0: continue #right edge
   #    board = area_fill(board, sp+d, dirs)
   puzzle2=wallarea(puzzle2,x+1,y)
   puzzle2=wallarea(puzzle2,x-1,y)
   puzzle2=wallarea(puzzle2,x,y+1)
   puzzle2=wallarea(puzzle2,x,y-1)
   return puzzle2
def isValid(puzzle2):
   b1=walls(puzzle2)
   b2=check3letters(puzzle2)
   #print(b1,b2)
   return b1 and b2
def make_move(block1,block2):
   puzzle2=[[x for x in row] for row in puzzle]
   puzzle2[block1[0]][block1[1]]=BLOCKCHAR
   puzzle2[block2[0]][block2[1]]=BLOCKCHAR
   return puzzle2
def recur():
   global puzzle
   if check_complete(): return puzzle
   for moves in possible_blocks():
      #display(puzzle)
      #print("?")
      if isValid(make_move(moves[0],moves[1])):
         #print(".")
         temp=[[x for x in row] for row in puzzle]
         puzzle=make_move(moves[0],moves[1])
         result=recur()
         if result!=None: return puzzle
         puzzle=[[x for x in row] for row in temp]
      else:
         puzzle[moves[0][0]][moves[0][1]]=PROTECTEDCHAR
         puzzle[moves[1][0]][moves[1][1]]=PROTECTEDCHAR
   return None

def select_unfilled_word():
   global start_dict
   min=100000000000000000000
   spot=""
   string=""
   for i in start_dict:
      for j in start_dict[i]:
         x,y,direction=j
         s=""
         for add in range(i):
            if direction=="V":
               s=s+puzzle[x+add][y]
            else:
               s=s+puzzle[x][y+add]
         possible=0
         reg=s.replace(OPENCHAR,".")
         for word in word_dict[i]:
            if re.match(reg,word):
               possible=possible+1
         if possible<min: 
            min=possible
            spot=j
            string=s
   #start_dict[len(string)].remove(spot)
   return spot,string
def num_possible_crosses(x,y,direction,start_list,ch):
   #print(x,y,direction)
   global puzzle
   x1,y1=x,y
   ch2=puzzle[x][y]
   puzzle[x][y]=ch
   while (x,y,direction) not in start_list:
      if direction=="V":
         x=x-1
      else:
         y=y-1
   s=""
   while x<columns and y<rows and puzzle[x][y]!=BLOCKCHAR:
      if direction=="V":
         s=s+puzzle[x][y]
         x=x+1
      else:
         s=s+puzzle[x][y]
         y=y+1
   reg=s.replace(OPENCHAR,".")
   #print(reg)
   count=0
   for word in word_dict[len(reg)]:
      if re.match(reg,word):
         #print("h")
         count=count+1
   #print(count)
   puzzle[x1][y1]=ch2
   return count
def pick_word(spot):
   tup,s=spot
   x,y,direction=tup
   length=len(s)
   #print(length)
   list=word_dict[length]
   candidates=[]
   count=0
   i=0
   reg=s.replace(OPENCHAR,".")
   #print(reg)
   n=int(math.sqrt(len(list))/2)
   while count<n and i<len(list):
      if re.match(reg,list[i]):
         count=count+1
         candidates.append(list[i])
      i=i+1
   #start_list=[]
   #print(candidates)
   # for i in start_dict:
   #    start_list=start_list+start_dict[i]
   #print("hi")
   newcands=[]
   for word in candidates:
      product=1
      for add in range(length):
         ch=word[add]
         if direction=="V" and puzzle[x+add][y]==OPENCHAR:
            num=num_possible_crosses(x+add,y,OPPOSITE_DIRECTION[direction],start_list,ch)
            #print(num)
            product=product*num
         elif direction=="H" and puzzle[x][y+add]==OPENCHAR:
            num=num_possible_crosses(x,y+add,OPPOSITE_DIRECTION[direction],start_list,ch)
            #print(num)
            product=product*num
      newcands.append((word,product))
   newcands.sort(key=lambda x:x[1],reverse=True)
   #print(newcands)
   return [p[0] for p in newcands if p[1]!=0]
   
def ordered_domain(candidates):
   return candidates   

def backtrack():
   global puzzle,word,word_dict,word_list,start_dict
   check=True
   for i in range(columns):
      for j in range(rows):
         if puzzle[i][j]==OPENCHAR:
            check=False
   if check: return puzzle
   spot,string=select_unfilled_word()
   print(spot,string)
   list=ordered_domain(pick_word((spot,string)))
   #print(list)
   for word in list:
      temp=[[x for x in row] for row in puzzle]
      print(spot[0],spot[1])
      placeword(word,spot[0],spot[1],spot[2])
      print(word)
      if word in word_dict[len(word)]:
         word_dict[len(word)].remove(word)
      if word not in word_list:
         word_list.remove(word)
      start_dict[len(string)].remove(spot)
      display(puzzle)
      result=backtrack()
      if result!=None: return puzzle
      puzzle=[[x for x in row] for row in temp]
      word_dict[len(word)].append(word)
      word_list.append(word)
      start_dict[len(string)].append(spot)
   return None

def solve():
   global puzzle
   if numblocks==rows*columns: 
      puzzle= [[BLOCKCHAR for i in range(columns)] for j in range(rows)]
      return
   fix180()
   while not check3letters(puzzle):
      illegal_gaps()
      fix180()
   #print(numblocks)
   if not walls(puzzle):
      temp=[[x for x in row] for row in puzzle]
      count=100000
      while count>numblocks or not walls(puzzle):
         puzzle=[[x for x in row] for row in temp]
         x,y=findopen2(puzzle)
         wallarea(puzzle,x,y)
         x,y=findopen2(puzzle)
         wallarea(puzzle,x,y)
         count=0
         for i in range(columns):
            for j in range(rows):
               if puzzle[i][j]==BLOCKCHAR: count=count+1
      #print(count,numblocks)
   #print(walls(puzzle))
   #display(puzzle)
   recur()
   for i in range(columns):
      for j in range(rows):
         if puzzle[i][j]==PROTECTEDCHAR:
            puzzle[i][j]=OPENCHAR
   start_positions()
   #backtrack()
#python c:\Users\steve\Documents\TJ\AI\assignments\Li_S_U4_L4.py 7x7 6 scrabble.txt V0x0come v0x1here h0x2ERS
#11x9 16 dct20k.txt V0x1Her
#9x9 81 dct20k.txt
#14x15 104 dct20k.txt H3x2 H2x3 H4x4 H7x4 v5x10 h4x7##
#10x15 32 dct20k.txt V6x0# V9x3# H3x11# V0x10Freshwater
#15x15 39 dct20k.txt H0x0Mute V0x0mule V10x13Sucks H7x5# V3x4# H6x7# V11x3#
#13x13 32 dct20k.txt H1x4#Toe# H9x2# V3x6# H10x0Scintillating V0x5stirrup H4x2##Ordained V0x1Hour V0x12Wes V5x0zoo
#7x4 0 dct20k.txt V0x0Walmart V0x3Modules
#9x12 32 dct20k.txt V5x0# V8x3# H3x8# V0x5Accompany
#16x16 184 dct20k.txt h3x2 H2x3 h4x4 V7x4
#4x4 0 "dct20k.txt"
#7x7 11 "dct20k.txt"
#python c:\Users\steve\Documents\TJ\AI\assignments\Li_S_U4_L4.py 11x9 16 dct20k.txt V0x1Her
#python c:\Users\steve\Documents\TJ\AI\assignments\Li_S_U4_L4.py 4x4 0 "dct20k.txt"
#python c:\Users\steve\Documents\TJ\AI\assignments\Li_S_U4_L4.py 5x5 0 "dct20k.txt" "V2x3i"
#python c:\Users\steve\Documents\TJ\AI\assignments\Li_S_U4_L4.py 5x5 0 "dct20k.txt" "H3x0scare"
#python c:\Users\steve\Documents\TJ\AI\assignments\Li_S_U4_L4.py 9x13 19 "dct20k.txt" "v2x3#" "v1x8#" "h3x1#" "v4x5##"
def main():
   input()
   #print(numblocks)
   #print(isValid(puzzle))
   # fix180()
   # while not isValid(puzzle):
   # illegal_gaps()
   # fix180()
   # print (isValid(puzzle))
   solve()
   display(puzzle)
   #print(average_word_length(puzzle))
   # print(start_dict)
   # print(puzzle[0])
   #print(start_dict)
   #print(pick_word(select_unfilled_word()))
   backtrack()
   print("Solution:")
   display(puzzle)
   #print(word_list)
   
if __name__=="__main__":
   main()
