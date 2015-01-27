import networkx as nx
import itertools as iter

f = open('result.txt','w')

"""
The next three lines simply set up some initial stuff; finding all permutations
of 1, 2, 3, 4 and storing them, making a list of labels a-x, and then combinging
them to make a dictionary that associates every letter with a permutation.
"""

permList = [list(i) for i in list(iter.permutations([1,2,3,4,]))]
permLabels = {i : j for i, j in iter.izip(range(24), permList)}

"""
Here are the functions for generating the neighbors of a permutation; I tried 
splitting up the work as much as possible so that if my algorithms are wrong you
can modify them relatively easily (hence the 'swap' 'fronttoback' etc.)
"""

def swap(List, indexA, indexB):
    List[indexA], List[indexB] = List[indexB], List[indexA]
    return List
    
def frontToBack(List):
    List.append(List.pop(0))
    return List
    
def backToFront(List):
    List.insert(0, List.pop())
    return List

def getLabel(dictionary, search):
    for key, value in dictionary.iteritems():
        if value == search:
            return key
                          
def makeNeighbors(perm):
    neighborList = [] 
    neighborLabels = [] 
    
    for i in range(len(perm)):
        neighbor = perm[:]
        if i == (len(perm)-1):
            neighborList.append(backToFront(neighbor))
            neighbor = perm[:]
            neighborList.append(frontToBack(neighbor))
        else:
            neighborList.append(swap(neighbor, i, i+1))
        
    currentTotal = len(neighborList)-1
            
    for i in range(0, currentTotal): 
        listCopy = neighborList[:]
        doubleSwap = listCopy[i][:]
        if i == 2:
            neighborList.append(backToFront(doubleSwap))   
        elif i == 3:
            neighborList.append(swap(doubleSwap, 0, 1))
            doubleSwap = listCopy[i][:]
            neighborList.append(backToFront(doubleSwap))
        elif i <= 1:
            neighborList.append(swap(doubleSwap, i+1, i+2))
    
    for neighbors in neighborList:
        neighborLabels.append(getLabel(permLabels, neighbors))
    return neighborLabels

allNeighbors = [makeNeighbors(i) for i in permList] 
  
"""
Now for the more Conway-ish things; getting every possible 24-bit string of 
0s and 1s in order to check every initial state, pairing them with the labels, 
and making a huge list of every possible initial state. Also here is the Conway
life/death algorithm itself, which will be run once on each initial state.
"""

bitStrings = ["".join(seq) for seq in iter.product("01", repeat = 24)]
bitStrings = bitStrings[8388608:12582912]
bitStrings = tuple(bitStrings)

"""
Copy the entire elif block below in the Conway function, and make sure the indentation is correct and consistent.
change the condition (elif i == something) to match the appropriate position you're checking (essentially
increase it by one each time you paste). Now, using the two dictionaries that are printed, change 
the bracketed numbers in variable total to match the numbers that correspond to the letters
in the neighbors lists. 
"""

def resultCalc(List, pos):
    global allNeighbors
    total = 0
    for i in allNeighbors[pos]:
        total += List[i]
    return total 

def Conway(bitNum):
    result = []
    bitNum = [int(i) for i in list(bitNum)]
    for i in range(len(bitNum)):
        if (bitNum[i] == 1 and (resultCalc(bitNum, i) == 2 or resultCalc(bitNum, i) ==3)) or (bitNum[i] == 0 and resultCalc(bitNum, i) == 3):
            result.append(1)
        else: 
            result.append(0)
    return result

"""
This part does all of the actual work you care about; it takes every 24-bit 
binary string, and applies the Conway algorithm to it until a loop is found. The
length of the loop is then appended to a global list variable that is then 
printed so you can see the lengths of every single cycle (considering there are
16 million or so this is a crazy list. A later optimization will be to remove 
all duplicate cycles, but this will require active checking of what particular
cycles have been attained with each new starting value.  
"""

for j in bitStrings:
    conwayGraph = nx.DiGraph()

    p1 = tuple([int(i) for i in list(j)])
    p2 = tuple(Conway(list(p1)))
    
    f.write('Starting String: ' + str(p1) + '\n')
    f.write('Number Alive: ' + str(sum(p1)) + '\n')
    

    for i in range(1, 100): 
        conwayGraph.add_node(p1)
        conwayGraph.add_node(p2)
        conwayGraph.add_edge(p1, p2)
        p1 = p2
        p2 = tuple(Conway(list(p2)))
        
    cycles = list(nx.simple_cycles(conwayGraph))
    f.write('Head Length: ' + str(len(conwayGraph)-len(cycles[0])) + '\n')
    f.write('Tail Length:' + str(len(cycles[0])))
    f.write('\n')
    f.write('\n')
