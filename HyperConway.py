import networkx as nx
import itertools as iter

f = open('result.txt','w')

"""
The next three lines simply set up some initial stuff; finding all permutations
of 1, 2, 3, 4 and storing them, making a list of labels a-x, and then combinging
them to make a dictionary that associates every letter with a permutation.
"""

permList = [list(i) for i in list(iter.permutations([1,2,3,4,]))]
labels = 'a b c d e f g h i j k l m n o p q r s t u v w x'.split()
permLabels = {i: j for i, j in iter.izip(labels, permList)}
letterNums = {i : j for i, j in iter.izip(labels, range(23))}

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
dictNeighbors = {i : j for i, j in iter.izip(labels, allNeighbors)}

# print dictNeighbors
# print letterNums
  
"""
Now for the more Conway-ish things; getting every possible 24-bit string of 
0s and 1s in order to check every initial state, pairing them with the labels, 
and making a huge list of every possible initial state. Also here is the Conway
life/death algorithm itself, which will be run once on each initial state.
"""

bitStrings = ["".join(seq) for seq in iter.product("01", repeat = 24)]
bitStrings = tuple(bitStrings)

"""
Copy the entire elif block below in the Conway function, and make sure the indentation is correct and consistent.
change the condition (elif i == something) to match the appropriate position you're checking (essentially
increase it by one each time you paste). Now, using the two dictionaries that are printed, change 
the bracketed numbers in variable total to match the numbers that correspond to the letters
in the neighbors lists. 
"""

def Conway(bitNum):
    result = []
    bitNum = [int(i) for i in list(bitNum)]
    for i in range(len(bitNum)):
        if i == 0:
            total = bitNum[6] + bitNum[2] + bitNum[1] + bitNum[18] + bitNum[9] + bitNum[8] + bitNum[3] + bitNum[12] + bitNum[4] + bitNum[16]
            if (bitNum[0] == 1 and (total == 2 or total ==3)) or (bitNum[0] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
                
        # Start copying here
        elif i == 1:
            total = bitNum[7] + bitNum[4] + bitNum[0] + bitNum[12] + bitNum[11] + bitNum[10] + bitNum[5] + bitNum[18] + bitNum[2] + bitNum[22]
            if (bitNum[1] == 1 and (total == 2 or total ==3)) or (bitNum[1] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        # End copying here
        
        elif i == 2:
            total = bitNum[12] + bitNum[0] + bitNum[3] + bitNum[19] + bitNum[15] + bitNum[14] + bitNum[1] + bitNum[6] + bitNum[5] + bitNum[10]
            if (bitNum[2] == 1 and (total == 2 or total ==3)) or (bitNum[2] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
                
        elif i == 3:
            total = bitNum[13] + bitNum[5] + bitNum[2] + bitNum[6] + bitNum[17] + bitNum[16] + bitNum[4] + bitNum[19] + bitNum[0] + bitNum[20]
            if (bitNum[3] == 1 and (total == 2 or total ==3)) or (bitNum[3] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)        
        
        elif i == 4:
            total = bitNum[12] + bitNum[0] + bitNum[3] + bitNum[19] + bitNum[15] + bitNum[14] + bitNum[1] + bitNum[6] + bitNum[5] + bitNum[10]
            if (bitNum[4] == 1 and (total == 2 or total ==3)) or (bitNum[4] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 5:
            total = bitNum[18] + bitNum[1] + bitNum[5] + bitNum[13] + bitNum[21] + bitNum[20] + bitNum[0] + bitNum[7] + bitNum[3] + bitNum[8]
            if (bitNum[5] == 1 and (total == 2 or total ==3)) or (bitNum[5] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0) 
        
        elif i == 6:
            total = bitNum[0] + bitNum[8] + bitNum[7] + bitNum[20] + bitNum[3] + bitNum[2] + bitNum[9] + bitNum[14] + bitNum[10] + bitNum[17]
            if (bitNum[6] == 1 and (total == 2 or total ==3)) or (bitNum[6] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 7:
            total = bitNum[1] + bitNum[10] + bitNum[6] + bitNum[14] + bitNum[5] + bitNum[4] + bitNum[11] + bitNum[20] + bitNum[8] + bitNum[23]
            if (bitNum[7] == 1 and (total == 2 or total ==3)) or (bitNum[7] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 8:
            total = bitNum[14] + bitNum[6] + bitNum[9] + bitNum[21] + bitNum[13] + bitNum[12] + bitNum[7] + bitNum[0] + bitNum[11] + bitNum[4]
            if (bitNum[8] == 1 and (total == 2 or total ==3)) or (bitNum[8] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 9:
            total = bitNum[15] + bitNum[11] + bitNum[8] + bitNum[0] + bitNum[16] + bitNum[17] + bitNum[10] + bitNum[21] + bitNum[6] + bitNum[18]
            if (bitNum[9] == 1 and (total == 2 or total ==3)) or (bitNum[9] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 10:
            total = bitNum[20] + bitNum[7] + bitNum[11] + bitNum[15] + bitNum[19] + bitNum[18] + bitNum[6] + bitNum[1] + bitNum[9] + bitNum[2]
            if (bitNum[10] == 1 and (total == 2 or total ==3)) or (bitNum[10] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 11:
            total = bitNum[21] + bitNum[9] + bitNum[10] + bitNum[1] + bitNum[22] + bitNum[23] + bitNum[8] + bitNum[15] + bitNum[7] + bitNum[12]
            if (bitNum[11] == 1 and (total == 2 or total ==3)) or (bitNum[11] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 12:
            total = bitNum[2] + bitNum[14] + bitNum[13] + bitNum[22] + bitNum[1] + bitNum[0] + bitNum[15] + bitNum[8] + bitNum[16] + bitNum[11]
            if (bitNum[12] == 1 and (total == 2 or total ==3)) or (bitNum[12] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        
        elif i == 13:
            total = bitNum[3] + bitNum[16] + bitNum[12] + bitNum[8] + bitNum[4] + bitNum[5] + bitNum[17] + bitNum[22] + bitNum[14] + bitNum[21]
            if (bitNum[13] == 1 and (total == 2 or total ==3)) or (bitNum[13] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 14:
            total = bitNum[8] + bitNum[12] + bitNum[15] + bitNum[23] + bitNum[7] + bitNum[6] + bitNum[13] + bitNum[2] + bitNum[17] + bitNum[5]
            if (bitNum[14] == 1 and (total == 2 or total ==3)) or (bitNum[14] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 15:
            total = bitNum[9] + bitNum[17] + bitNum[14] + bitNum[2] + bitNum[10] + bitNum[11] + bitNum[16] + bitNum[23] + bitNum[12] + bitNum[19]
            if (bitNum[15] == 1 and (total == 2 or total ==3)) or (bitNum[15] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 16:
            total = bitNum[22] + bitNum[13] + bitNum[12] + bitNum[9] + bitNum[18] + bitNum[19] + bitNum[12] + bitNum[3] + bitNum[15] + bitNum[0]
            if (bitNum[16] == 1 and (total == 2 or total ==3)) or (bitNum[16] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 17:
            total = bitNum[23] + bitNum[15] + bitNum[16] + bitNum[3] + bitNum[20] + bitNum[21] + bitNum[14] + bitNum[9] + bitNum[13] + bitNum[6]
            if (bitNum[17] == 1 and (total == 2 or total ==3)) or (bitNum[17] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 18:
            total = bitNum[8] + bitNum[20] + bitNum[19] + bitNum[16] + bitNum[0] + bitNum[1] + bitNum[21] + bitNum[10] + bitNum[22] + bitNum[9]
            if (bitNum[18] == 1 and (total == 2 or total ==3)) or (bitNum[18] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 19:
            total = bitNum[5] + bitNum[22] + bitNum[18] + bitNum[10] + bitNum[2] + bitNum[3] + bitNum[23] + bitNum[16] + bitNum[20] + bitNum[15]
            if (bitNum[19] == 1 and (total == 2 or total ==3)) or (bitNum[19] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 20:
            total = bitNum[10] + bitNum[18] + bitNum[21] + bitNum[17] + bitNum[6] + bitNum[7] + bitNum[19] + bitNum[4] + bitNum[23] + bitNum[3]
            if (bitNum[20] == 1 and (total == 2 or total ==3)) or (bitNum[20] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 21:
            total = bitNum[11] + bitNum[23] + bitNum[20] + bitNum[4] + bitNum[8] + bitNum[9] + bitNum[22] + bitNum[17] + bitNum[18] + bitNum[13]
            if (bitNum[21] == 1 and (total == 2 or total ==3)) or (bitNum[21] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 22:
            total = bitNum[16] + bitNum[19] + bitNum[23] + bitNum[11] + bitNum[12] + bitNum[13] + bitNum[18] + bitNum[5] + bitNum[21] + bitNum[1]
            if (bitNum[22] == 1 and (total == 2 or total ==3)) or (bitNum[22] == 0 and total == 3):
                result.append(1)
            else: 
                result.append(0)
        
        elif i == 23:
            total = bitNum[17] + bitNum[21] + bitNum[22] + bitNum[5] + bitNum[14] + bitNum[15] + bitNum[20] + bitNum[11] + bitNum[19] + bitNum[7]
            if (bitNum[23] == 1 and (total == 2 or total ==3)) or (bitNum[23] == 0 and total == 3):
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

    for i in range(1, 100): 
        conwayGraph.add_node(p1)
        conwayGraph.add_node(p2)
        conwayGraph.add_edge(p1, p2)
        p1 = p2
        p2 = tuple(Conway(list(p2)))
        
    cycles = list(nx.simple_cycles(conwayGraph))
    f.write(len(cycles[0]))
    f.write('\n')