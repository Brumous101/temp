# Kyle
# Huffman Algorithm for data compression
from typing import List


index = 0

class Node(object):
    def __init__(self,char,freq=1, left= None, right= None, leftchildren = [], rightchildren =[]):
        self.character = char
        self.frequency = freq
        self.left_child = left
        self.right_child = right
        self.left_children = leftchildren
        self.right_children = rightchildren

f = open('uncompressed-file.txt','r')
dictionary ={
}
flist = []
counter = 1
def startList():
    c = f.read(1)
    flist.append(Node(c))

def continueList():
    while True:
        c = f.read(1)
        i = 0
        while i < len(flist):
            if flist[i].character == c:
                flist[i].frequency = flist[i].frequency + 1
                break
            # Reached the end of the list and char not found
            i =  i + 1
            if i == len(flist):
                flist.append(Node(c))
                break
        if not c:
            print("End of file")
            break
def buildTree():
    x = 0
    y = 0
    while x < len(flist):
        flist.sort(key=lambda z: z.frequency)
        name = "Node" + str(y)
        if x < (len(flist) - 1):
            num = flist[x].frequency + flist[x+1].frequency
            lchildren = []
            rchildren = []
            # If it's not a leaf
            if flist[x].left_child != None and flist[x+1].right_child != None:
                lchildren = flist[x].left_children + flist[x].right_children
                rchildren = flist[x+1].left_children + flist[x+1].right_children
            # It's joining a node and a leaf or 2 leafs
            else:
                lchildren.append(flist[x].left_child.character)
                rchildren
            flist.append(Node(name, num, flist[x], flist[x+1], lchildren, rchildren))
            #flist[len(flist)-1].children.append()
            print(flist[len(flist)-1].character) 
            #print("left name:"+flist[(len(flist))-1].left_child.character + " right name:" + flist[(len(flist))-1].right_child.character)
            print(" Left Children ",end="")
            for a in flist[len(flist)-1].left_children:
                print(a,end="")
            print()
            print(" Right Children ",end="")
            for a in flist[len(flist)-1].right_children:
                print(a,end="")
            print()
        else:
            num = flist[x].frequency
            flist.append(Node(name, num, flist[x]))
        x = x + 2
        y = y + 1

def compressData():
    startNode = flist[len(flist) - 1]
    cur = startNode
    #print(cur.left_child.character)



startList()
continueList()
flist.sort(key=lambda x: x.frequency)
buildTree()
# for i in range(len(flist)):
#     if ((flist[i].left_child != None) and (flist[i].right_child != None)):
#         print("Parent " + str(flist[i].character) + " " + "left " + str(flist[i].left_child.character) +" "+ " right " + str(flist[i].right_child.character))
#for i in range(len(flist)):
#    print()
#    print("Node: " + str(flist[i].character))
#    print("left_children: ")
#    for x in range(len(flist[i].left_children)):
#        print( flist[i].left_children[x] + " ",end="")
#    print()
#    print("right_children: ")
#    for y in range(len(flist[i].left_children)):
#        print(flist[i].right_children[y] + " ", end ="")
# for i in range(len(flist)):
#     print(flist[i].character + )
compressData()