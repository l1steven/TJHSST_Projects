# Name: Steven Li
# Date: 12/2/2020
import os, time
import copy
from queue import PriorityQueue
def check_complete(assignment):
   return "." not in assignment
   
def select_unassigned_var(assignment, variables):
   vars={k:variables[k].copy() for k in variables}
   for i in range(81):
       if assignment[i]!="." and i in vars: del vars[i]
   return min(vars,key=lambda x: len(vars[x]))

   # minList=min(vars.values(),key=len)
   # i=list(vars.keys())[list(vars.values()).index(minList)]
   # b=True
   # while b:
   #    if check_complete(assignment): break
   #    i=min(vars,key=lambda x: len(vars[x]))
   #    if len(vars[i])==1:
   #       assignment=assignment[:i]+vars[i][0]+assignment[i+1:]
   #       del vars[i]
   #    else: b=False
   # return i
   #return i
   # m=100
   # index=0
   # for i,char in enumerate(assignment):
   #    if min==1:
   #       break
   #    if char==".":
   #       a=len(variables[i])
   #       if a<m:
   #          m=a
   #          index=i
   # return index


def isValid(value, var_index, assignment, variables,neighbors, csp_table):
   # for box in csp_table:
   #    if var_index in box:
   #       for i in box:
   #          if assignment[i]==value: return False
   # return True
   for i in neighbors[var_index]:
      if assignment[i]==value:return False
   return True
def constrained_neighbors(val,var,variables,neighbors):
   x=0
   for neighbor in neighbors[var]:
      if val in variables[neighbor]: x=x+1
   return x
def ordered_domain(assignment, var,variables, neighbors,q_table):
   # minimum=100
   # lcv=1
   # myList=[]
   # for val in variables[var]:
   #    x=0
   #    for neighbor in neighbors[var]:
   #       if val in variables[neighbor]: x=x+1
   #    # if x<minimum: 
   #    #    minimum=x
   #    #    lcv=val
   #    myList.append((val,x))
   #    myList.sort(key=lambda x:x[1])
   # return [tup[0] for tup in myList]
   #variables[var].sort(key=lambda val: constrained_neighbors(val,var,variables,neighbors))
   #return variables[var]
   # myList=[]
   # for q in q_table:
   #    if q in variables: myList.append((q,q_table[q]))
   # myList.sort(key=lambda x: x[1])
   # return [tup[0] for tup in myList]
   return variables[var]

       


def update_variables(value,var_index, assignment,neighbors, variables,q_table):
   #for value in variables[var_index]:
   for i in neighbors[var_index]:
      if value in variables[i]: variables[i].remove(value)
   #variables.pop(var_index)
   #q_table[value]=q_table[value]+1
   #variables.pop(var_index)
   #return {}
   # for i in range(81):
   #    if len(variables[i])==1:
   #       assignment=assignment[:i]+variables[i][0]+assignment[i+1:]

#def backtracking_search(puzzle, variables, csp_table): 
#   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, neighbors,q_table):
   if check_complete(assignment): return assignment
   var=select_unassigned_var(assignment,variables)
   # if len(variables[var])==1:
   #    puzzle=puzzle[:i]+variables[i][0]+puzzle[i+1:]
   #    del variab
   #update_variables(var,assignment,neighbors,variables,csp_table)
   for value in ordered_domain(assignment,var,variables,neighbors,q_table ):
       #isValid(value,var,assignment,variables,neighbors,csp_table):
         varsTemp={k:variables[k].copy() for k in variables}
         update_variables(value, var,assignment,neighbors,varsTemp,q_table)
         temp=assignment
         assignment=assignment[:var]+value+assignment[var+1:]
         result=recursive_backtracking(assignment,varsTemp,neighbors,q_table)
         if result: return result
         assignment=temp
         
         #update_variables(value,var,assignment,neighbors,variables,csp_table)

   return None

def initialize_ds(puzzle,neighbors):
   variables={}
   for i in range(81):
      if puzzle[i]==".":
         variables[i]=["1","2","3","4","5","6","7","8","9"]
      else:
         variables[i]=[puzzle[i]]
   for j in range(9):
      for i in range(81):
         if len(variables[i])==1:
            for p in neighbors[i]:
               if variables[i][0] in variables[p]:variables[p].remove(variables[i][0])
               # for j in variables[i]:
               #    if j in variables[p]: variables[p].remove(j)
   # for i in range(81):
   #    if len(variables[i])==1:
   #       puzzle=puzzle[:i]+variables[i][0]+puzzle[i+1:]
   q_table={}
   # for i in "123456789":
   #    q_table[i]=puzzle.count(i)

   return variables,puzzle,q_table

def solve(puzzle, neighbors): 
   ''' suggestion:
   # q_table is quantity table {'1': number of value '1' occurred, ...}
   variables, puzzle, q_table = initialize_ds(puzzle, neighbors)  
   return recursive_backtracking(puzzle, variables, neighbors, q_table)
   '''
   variables,puzzle,q_table=initialize_ds(puzzle,neighbors)

   return recursive_backtracking(puzzle,variables,neighbors,q_table)

def sudoku_neighbors(csp_table):
   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   d={}
   for i in range(81):
      l=[]
      for j in csp_table:
         if i in j:
            for k in j:
               if k not in l and k!=i: l.append(k)
      d[i]=l
   return d
   
def sudoku_csp(n=9):
   csp_table = [[k for k in range(i*n, (i+1)*n)] for i in range(n)] # rows
   csp_table += [[k for k in range(i,n*n,n)] for i in range(n)] # cols
   temp = [0, 1, 2, 9, 10, 11, 18, 19, 20]
   csp_table += [[i+k for k in temp] for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]] # sub_blocks
   return csp_table

def checksum(solution):
   return sum([ord(c) for c in solution]) - 48*81 # One easy way to check a valid solution

def main():
   filename = input("file name: ")
   if not os.path.isfile(filename):
      filename = "puzzles.txt"
   csp_table = sudoku_csp()   # rows, cols, and sub_blocks
   neighbors = sudoku_neighbors(csp_table)   # each position p has its neighbors {p:[positions in same row/col/subblock], ...}
   start_time = time.time()
   for line, puzzle in enumerate(open(filename).readlines()):
      if line == 128: break  # check point: goal is less than 0.5 sec
      line, puzzle = line+1, puzzle.rstrip()
      print ("Line {}: {}".format(line, puzzle)) 
      solution = solve(puzzle, neighbors)
      if solution == None:print ("No solution found."); break
      print ("{}({}, {})".format(" "*(len(str(line))+1), checksum(solution), solution))
   print ("Duration:", (time.time() - start_time))

if __name__ == '__main__': main()