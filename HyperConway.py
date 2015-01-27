import itertools as iter

"""
The next three lines simply set up some initial stuff; finding all permutations
of 1, 2, 3, 4 and storing them, making a list of labels a-x, and then combinging
them to make a dictionary that associates every letter with a permutation.
"""

permLis = [list(i) for i in list(iter.permutations([5,1,2,3,4,]))]
permList = []
for z in permLis:
    if z[0] == 5:
        permList.append(z)
permLabels = dict(enumerate(permList))
"""
Here are the functions for generating the neighbors of a permutation; I tried 
splitting up the work as much as possible so that if my algorithms are wrong you
can modify them relatively easily (hence the 'swap' 'fronttoback' etc.)
"""
def normalize(p,q):
    p = p[p.index(q):] + p[:p.index(q)]
    return p
    
def rotateLeft(P,k):
    P = P[k:] + P[:k]
    return P
    
def swap(L,k):
    L = L[:k] + [L[k+1],L[k]] + L[k+2:]
    return L

def getLabel(dictionary, search):
    for key, value in dictionary.iteritems():
        if value == search:
            return key
                          
def makeNeighbors(perm):
    neighborList = [] 
    neighborLabels = [] 
    
    for k in range(5):
        neighborList.append(normalize(swap(rotateLeft(perm,k),0),5))
        j = swap(rotateLeft(perm,k),0)
        neighborList.append(normalize(swap(j,2),5))
    
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

def liveNeighbors(List, pos):
    global allNeighbors
    total = 0
    for i in allNeighbors[pos]:
        total += List[i]
    return total 

def Conway(bitNum):
    result = []
    bitNum = [int(i) for i in list(bitNum)]
    for i in range(len(bitNum)):
        if (bitNum[i] == 1 and (liveNeighbors(bitNum, i) == 2 or liveNeighbors(bitNum, i) ==3)) or (bitNum[i] == 0 and liveNeighbors(bitNum, i) == 3):
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
if __name__ == "__main__":
    bitStrings = ["".join(seq) for seq in iter.product("01", repeat = 24)]
    #bitStrings = bitStrings[8388608:12582912]
    bitStrings = tuple(bitStrings)
    f = open('result.txt','w')
    f.write('[Number,StartingConfig,NumberAlive,HeadLength,TailLength' + '\n')
    start = 1
    for j in bitStrings:
        starting = [int(i) for i in list(j)]
        seen = [starting]
        p1 = tuple([int(i) for i in list(j)])
        f.write('[#' + str(start) + ',')
        start += 1
        f.write(str(p1) + ',')
        f.write(str(sum(p1)) + ',')
        while True:
            j = Conway(j)
            if j in seen:
                f.write(str(len(seen[:seen.index(j)])) + ',')
                f.write(str(len(seen[seen.index(j):])))
                f.write(']' + '\n')
                break
            else:
                seen.append(j)
