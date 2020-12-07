import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness, calculate_happiness_for_room, calculate_stress_for_room, convert_dictionary
import sys
import random
import time
import glob
import sys
import sys
import os
import json
from parse import validate_file

## put people into rooms while satisfying the stress constraint
#i is the ith edge to first pop 
def solve(G, s, c):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """
    k = 1 #number of breakout rooms opened currently
    totalPpl = G.number_of_nodes()
    BreakOutDict = {} #{key: breakoutRoomnNmber; value:list of people in that room}
    for i in range(10): #HARDCODE the range value to be number of breakoutRooms 1<=range<=totalPpl
        BreakOutDict[i] = []
    l = [] #people already put into rooms
    #sorted by decreasing value of (happ - stress)
    happyList = sorted(nx.Graph(G).edges, key = lambda a: nx.Graph(G).edges[a]["happiness"] - nx.Graph(G).edges[a]["stress"] , reverse = True)
    happiestEdge = happyList.pop(c)
    #print(happiestEdge)
    while len(l) != totalPpl: #break when all the people are placed in the rooms
        if len(happyList) == 0:
            #print("list is empty")
            return {}, -1
        happiestEdge = happyList.pop(random.randint(0, (int)(len(happyList)/4)))
        currStudent  = happiestEdge[0] #highest happiness pair
        currStudent2 = happiestEdge[1]
        if currStudent in l and currStudent2 in l:
            #print("continue")
            if len(happyList) != 0:
                happiestEdge = happyList.pop(random.randint(0, (int)(len(happyList)/4)))
                continue
            else:
                return {}, -1
        found = False
        #currRoom = 0
        maxHappyRoomNum = 0
        maxSumAllRmHapp = 0
        #loops through all the rooms opened, put the pair in the room that satisfies the stress constraint and that maximizes the happiness in all rooms
        for currRoom in range(0, k) : 
            addUniqueElements(BreakOutDict[currRoom], currStudent, currStudent2)
            if calculate_stress_for_room(BreakOutDict[currRoom] , G) < s/k and sumHappinessOverAllRooms(BreakOutDict, G) > maxSumAllRmHapp and checkStressConsForAllRoomsHaveOpened(BreakOutDict, s, k): #stress constraints satisfied so add currStudent and currStudent2
                found = True 
                maxHappyRoomNum = currRoom
                #print("found breakout room in range")
            removeIfnotInList(l,BreakOutDict[currRoom], currStudent, currStudent2)

        if found:
            addUniqueElements(BreakOutDict[maxHappyRoomNum], currStudent, currStudent2)
            addUniqueElements(l, currStudent, currStudent2)  #add the two to the list of people already put into rooms
        else:  #if all the rooms that have been opened won't satisfy the constraint, open a new room to put the two pairs
            k = k + 1 #new room
            if k >= 10:
                return {}, -1
            addUniqueElements(BreakOutDict[k - 1], currStudent, currStudent2)
            if checkStressConsForAllRoomsHaveOpened(BreakOutDict, s, k): #check if all constraints are satisfied
                #print("opened a new room")
                addUniqueElements(l, currStudent, currStudent2)  #add the two to the list of people already put into rooms
            else : #if opening a new breakroom fails, we decrease k back to where it used to be and do whileLoop again
                removeIfnotInList(l,BreakOutDict[k - 1], currStudent, currStudent2)
                k = k - 1 #we increased above so decrease k back 
                #print("loops again for a new happiest edge")
            #OR WE CAN try to split the two
    #z = str(len(l))
    #print("length of l rn is = " + z)
    return convert_dictionary(BreakOutDict), k 

    #check if stress constraint satisfied for all rooms up till the kth room(excluding)
def solve2(G, s, c):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """
    k = 1 #number of breakout rooms opened currently
    totalPpl = G.number_of_nodes()
    BreakOutDict = {} #{key: breakoutRoomnNmber; value:list of people in that room}
    for i in range(5): #HARDCODE the range value to be number of breakoutRooms 1<=range<=totalPpl
        BreakOutDict[i] = []
    l = [] #people already put into rooms
    #sorted by decreasing value of (happ - stress)
    happyList = sorted(nx.Graph(G).edges, key = lambda a: nx.Graph(G).edges[a]["happiness"]  , reverse = True)
    happiestEdge = happyList.pop(c)
    #print(happiestEdge)
    while len(l) != totalPpl: #break when all the people are placed in the rooms
        if len(happyList) == 0:
            #print("list is empty")
            return {}, -1
        happiestEdge = happyList.pop(random.randint(0, (int)(len(happyList)/4)))
        currStudent  = happiestEdge[0] #highest happiness pair
        currStudent2 = happiestEdge[1]
        if currStudent in l and currStudent2 in l:
            #print("continue")
            if len(happyList) != 0:
                happiestEdge = happyList.pop(random.randint(0, (int)(len(happyList)/4)))
                continue
            else:
                return {}, -1
        found = False
        #currRoom = 0
        maxHappyRoomNum = 0
        maxSumAllRmHapp = 0
        #loops through all the rooms opened, put the pair in the room that satisfies the stress constraint and that maximizes the happiness in all rooms
        for currRoom in range(0, k) : 
            addUniqueElements(BreakOutDict[currRoom], currStudent, currStudent2)
            if calculate_stress_for_room(BreakOutDict[currRoom] , G) < s/k and sumHappinessOverAllRooms(BreakOutDict, G) > maxSumAllRmHapp and checkStressConsForAllRoomsHaveOpened(BreakOutDict, s, k): #stress constraints satisfied so add currStudent and currStudent2
                found = True 
                maxHappyRoomNum = currRoom
                #print("found breakout room in range")
            removeIfnotInList(l,BreakOutDict[currRoom], currStudent, currStudent2)

        if found:
            addUniqueElements(BreakOutDict[maxHappyRoomNum], currStudent, currStudent2)
            addUniqueElements(l, currStudent, currStudent2)  #add the two to the list of people already put into rooms
        else:  #if all the rooms that have been opened won't satisfy the constraint, open a new room to put the two pairs
            k = k + 1 #new room
            addUniqueElements(BreakOutDict[k - 1], currStudent, currStudent2)
            if checkStressConsForAllRoomsHaveOpened(BreakOutDict, s, k): #check if all constraints are satisfied
                #print("opened a new room")
                addUniqueElements(l, currStudent, currStudent2)  #add the two to the list of people already put into rooms
            else : #if opening a new breakroom fails, we decrease k back to where it used to be and do whileLoop again
                removeIfnotInList(l,BreakOutDict[k - 1], currStudent, currStudent2)
                k = k - 1 #we increased above so decrease k back 
                #print("loops again for a new happiest edge")
            #OR WE CAN try to split the two
    #z = str(len(l))
    #print("length of l rn is = " + z)
    
    return convert_dictionary(BreakOutDict), k 

def sumHappinessOverAllRooms(dic, G):
    sum = 0
    for room in dic:
        sum += calculate_happiness_for_room(dic[room], G)
    return sum

#loop through all k rooms to check the stress constraint
def checkStressConsForAllRoomsHaveOpened(dic, s, k) :
    for i in range(0, k):
        if calculate_stress_for_room(dic[i] , G) >= s/k:
            return False
    return True

#calls solve() and loops steps number of times
def greedySolve(G,s):
    popIndex = 0
    while popIndex < len(G.edges): #can change the popIndex
        for steps in range(0, 50):
            dic, k = solve(G, s, popIndex) 
            """ dic2, k2 = solve2(G, s, popIndex)
            if len(dic) != 0 and is_valid_solution(dic,G, s, k) and len(dic2) != 0 and is_valid_solution(dic2, G, s, k2):
                solver1 = calculate_happiness(dic, G)
                solver2 = calculate_happiness(dic2, G)
                if solver1 < solver2:
                    print("for greedySolver ", dic, k)
                    return dic, k
                else:
                    print("for greedySolver2", dic2, k2)
                    return dic2, k2
                return dic, k
            elif len(dic) != 0 and is_valid_solution(dic,G, s, k):
                print("for greedySolver", dic, k)
                return dic, k
            elif len(dic2) != 0 and is_valid_solution(dic2, G, s, k2) :
                print("for greedySolver2", dic2, k2)
                return dic2, k2 """
            if len(dic) != 0 and is_valid_solution(dic,G, s, k):
                print("for greedySolver", dic, k)
                return dic, k
        popIndex = popIndex + 1
    print("for greedySolver FAILED to FIND SOL")
    return {}, 1

#if elem is not in arr, we can remove it from arr2
def removeIfnotInList(arr, arr2, elem1, elem2):
    if elem1 not in arr: 
        arr2.remove(elem1)
    if elem2 not in arr:
        arr2.remove(elem2)

#add elem if it is not in arr
def addUniqueElements(arr, elem1, elem2):
    if elem1 not in arr:
        arr.append(elem1)
    if elem2 not in arr:
        arr.append(elem2)
   

# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in
if __name__ == '__main__':
    inputs = glob.glob('inputs2/medium*')
    #inputs = glob.glob('inputs2/medium*')
    for input_path in inputs:
        print(input_path)
        output_path = 'outputs2/5' + input_path[8:-3] + '.out'
        #output_path = 'outputs2/5' + input_path[8:-3] + '.out'
        print(output_path)
        G, s = read_input_file(input_path)
        D, k = greedySolve(G, s)
        cost_t = calculate_happiness(D, G)
        write_output_file(D, output_path)

# Here's an example of how to run your solver.
#python3 solver2.py small-83.in
# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G, s = read_input_file(path)
#     D, k = solve(G, s)
#     assert is_valid_solution(D, G, s, k)
#     print("Total Happiness: {}".format(calculate_happiness(D, G)))
#     write_output_file(D, 'outputs/small-1.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('inputs/*')
#     for input_path in inputs:
#         output_path = 'outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G, s = read_input_file(input_path)
#         D, k = solve(G, s)
#         assert is_valid_solution(D, G, s, k)
#         happiness = calculate_happiness(D, G)
#         write_output_file(D, output_path)