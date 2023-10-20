# Name: Steven Li
# Date: 10/18/2020
import time
import string
def generate_adjacents(current, words_set):
   ''' words_set is a set which has all words.
   By comparing current and words in the words_set,
   generate adjacents set of current and return it'''
   adj_set = set()
   # TODO 1: adjacents
   # Your code goes here
   #c=list(current)
   for i in range(len(current)):
      for s in string.ascii_lowercase:
         new=current[:i]+s+current[i+1:]
         if new in words_set and new!=current: adj_set.add(new)

   return adj_set

def check_adj(words_set):
   # This check method is written for words_6_longer.txt
   adj = generate_adjacents('listen', words_set)
   target =  {'listee', 'listel', 'litten', 'lister', 'listed'}
   return (adj == target)

def findPath(start,goal,met,explored,backexplored):
   fhalf=[]
   bhalf=[]
   current=met
   while explored[current]!="s":
      fhalf.append(current)
      current=explored[current]
   current=met
   while backexplored[current]!="s":
      bhalf.append(current)
      current=backexplored[current]
   fhalf=fhalf[::-1]
   fhalf.pop()
   return [start]+fhalf+bhalf+[goal]

def bi_bfs(start, goal, words_set):
   '''The idea of bi-directional search is to run two simultaneous searches--
   one forward from the initial state and the other backward from the goal--
   hoping that the two searches meet in the middle. 
   '''
   if start == goal: return []
   # TODO 2: Bi-directional BFS Search
   # Your code goes here
   frontier=[start]
   backtier=[goal]
   explored = {start:"s"}
   backexplored={goal:"s"}
   while len(frontier)!=0 and len(frontier)!=0: 
      forwardpath=frontier.pop(0)
      if forwardpath in backtier: return findPath(start,goal,forwardpath,explored,backexplored)
      for child in generate_adjacents(forwardpath,words_set):
         if child not in explored: 
            frontier.append(child)
            explored[child]=forwardpath
      backpath=backtier.pop(0)
      if backpath in frontier: return findPath(start,goal,backpath,explored,backexplored)
      for child in generate_adjacents(backpath,words_set):
         if child not in backexplored:
            backtier.append(child)
            backexplored[child]=backpath
   return None

def main():
   filename = input("Type the word file: ")
   words_set = set()
   file = open(filename, "r")
   for word in file.readlines():
      words_set.add(word.rstrip('\n'))
   print ("Check generate_adjacents():", check_adj(words_set))
   initial = input("Type the starting word: ")
   goal = input("Type the goal word: ")
   cur_time = time.time()
   path = (bi_bfs(initial, goal, words_set))
   if path != None:
      print (path)
      print ("The number of steps: ", len(path))
      print ("Duration: ", time.time() - cur_time)
   else:
      print ("There's no path")
 
if __name__ == '__main__':
   main()

'''
Sample output 1
Type the word file: words.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'listed', 'fisted', 'fitted', 'fitter', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  9
Duration: 0.0

Sample output 2
Type the word file: words_6_longer.txt
Type the starting word: listen
Type the goal word: beaker
['listen', 'lister', 'bister', 'bitter', 'better', 'beater', 'beaker']
The number of steps:  7
Duration: 0.000997304916381836

Sample output 3
Type the word file: words_6_longer.txt
Type the starting word: vaguer
Type the goal word: drifts
['vaguer', 'vagues', 'values', 'valves', 'calves', 'cauves', 'cruves', 'cruses', 'crusts', 'crufts', 'crafts', 'drafts', 'drifts']
The number of steps:  13
Duration: 0.0408782958984375

Sample output 4
Type the word file: words_6_longer.txt
Type the starting word: klatch
Type the goal word: giggle
['klatch', 'clatch', 'clutch', 'clunch', 'glunch', 'gaunch', 'paunch', 'paunce', 'pawnce', 'pawnee', 'pawned', 'panned', 'panged', 'ranged', 'ragged', 'raggee', 'raggle', 'gaggle', 'giggle']
The number of steps:  19
Duration:  0.0867915153503418
'''