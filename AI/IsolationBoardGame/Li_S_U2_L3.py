# Name: Steven Li
# Date: 11/13/2020

def check_complete(assignment, csp_table):
   if "." in assignment: return False
   return True
   
def select_unassigned_var(assignment, variables, csp_table):
   return assignment.find(".")

def isValid(value, var_index, assignment, variables, csp_table):
   for box in csp_table:
      if var_index in box:
         for i in box:
            if assignment[i]==value: return False
   rowIndex=var_index-(var_index%9)
   stop=rowIndex
   while rowIndex<stop+9:
      if assignment[rowIndex]==value: return False
      rowIndex=rowIndex+1
   colIndex=var_index%9
   while colIndex<81:
      if assignment[colIndex]==value: return False
      colIndex=colIndex+9
   return True

def ordered_domain(assignment, variables, csp_table):
   return list("123456789")

def update_variables(value, var_index, assignment, variables, csp_table):
   return {}

def backtracking_search(puzzle, variables, csp_table): 
   return recursive_backtracking(puzzle, variables, csp_table)

def recursive_backtracking(assignment, variables, csp_table):
   if check_complete(assignment,csp_table): return assignment
   var=select_unassigned_var(assignment,variables,csp_table)
   for value in ordered_domain(assignment,variables,csp_table):
      if isValid(value,var,assignment,variables,csp_table):
         temp=assignment
         assignment=assignment[:var]+value+assignment[var+1:]
         result=recursive_backtracking(assignment,variables,csp_table)
         if result!=None: return result
         assignment=temp
   return None

def display(solution):
   s=""
   for i in range(len(solution)):
      s=s+solution[i]
      if i%27==26: s=s+"\n"*2
      elif i%9==8: s=s+"\n"
      elif i%3==2: s=s+" "
   return s

def sudoku_csp():
   return [[0,1,2,9,10,11,18,19,20],[3,4,5,12,13,14,21,22,23],[6,7,8,15,16,17,24,25,26],[27,28,29,36,37,38,45,46,47],[30,31,32,39,40,41,48,49,50]
   ,[33,34,35,42,43,44,51,52,53],[54,55,56,63,64,65,72,73,74],[57,58,59,66,67,68,75,76,77],[60,61,62,69,70,71,78,79,80]]

def initial_variables(puzzle, csp_table):
   return {}
   
def main():
   puzzle = input("Type a 81-char string:") 
   while len(puzzle) != 81:
      print ("Invalid puzzle")
      puzzle = input("Type a 81-char string: ")
   csp_table = sudoku_csp()
   variables = initial_variables(puzzle, csp_table)
   print ("Initial:\n" + display(puzzle))
   solution = backtracking_search(puzzle, variables, csp_table)
   if solution != None: print ("solution\n" + display(solution))
   else: print ("No solution found.\n")
   
if __name__ == '__main__': main()