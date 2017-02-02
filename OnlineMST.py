from random import *
from time import time
import cProfile



class Graph:
    
    def __init__(self):
        
        self.e = set()
        self.v = set()
        
    def addEdge(self,V1,V2):
        
        if V1 not in self.v:
            self.v = self.v | set([V1])

        if V2 not in self.v:
            self.v = self.v | set([V2])

        for (u,v,w) in self.e:
            if ((u == V1) and (v == V2)) or ((u == V2) and (v == V1)):
                return

        w = uniform(0,1)
        self.e = self.e | set([(V1, V2 , w)]) 
    
    def addEdges(self,V,E):
        
        self.v = set(V)
        self.e = set(E)
   
    def getEdges(self):
        
        return list(self.e)
    
    def sortedEdges(self):
        e = self.getEdges()
        return sorted(e, key=getWeight)
    
    def __str__(self):
        
        return str(self.e)
    
    def __repr__(self):
        
        return str(self.sortedEdges())    
    
    def getWeight(e):
        
        return e[2]

    def addNodes(self, size):
        V = [str(i) for i in range(size)]
        for node in V:
            self.v.add(node)
                 
    def addEdgesForOneNode(self, V1):
        for V2 in self.v:
            if V2 != V1:
                self.addEdge(V1, V2)

    def clearCycleEdges(self, setOfEdgesTaken, setOfNodes):
        setOfAllEdges = set()
        for node1 in setOfNodes:
            for node2 in setOfNodes:
                if (node1 != node2):
                    setOfAllEdges.add(self.getEdge(node1, node2))
        
        return (setOfAllEdges - setOfEdgesTaken)

    def getEdge(self, V1, V2):
        for (u,v,w) in self.e:
            if ((u == V1) and (v == V2)) or ((u == V2) and (v == V1)):
                return (u,v,w)

    def getEdgeWeight(self, V1, V2):
        for (u,v,w) in self.e:
            if ((u == V1) and (v == V2)) or ((u == V2) and (v == V1)):
                return w

    def takeMinEdge(self, set1, set2): #min edge from two set of nodes
        node1=set1.pop()
        node2=set2.pop()
        minEdge = self.getEdge(node1, node2)
        set1.add(node1)
        set2.add(node2)
        
        for node1 in set1:
            for node2 in set2:
                if self.getEdge(node1, node2) < minEdge:
                    minEdge = self.getEdge(node1, node2)
        return minEdge

    def takeMinOutEdgeNode(self, node):

        minEdge = ('0','0', 1.5)
        for (u,v,w) in self.e:
            if(u==node) and (w < minEdge[2]):
                minEdge = (u,v,w)
                
        return minEdge

    def initDict(self):
        d = {}
        for node in self.v:
            d[node] = float("inf")
        d['1'] = 0
        return d
        

def MST(G):
    taken = set()
    notTaken = G.v
    d = G.initDict()
    
    while len(d) != 0:
        
    
    return d

def getMinDict(d):
    return min(d, key=d.get)
            

def foo():
    t = time()
    G = Graph()
    #print(time() - t)
    G.addNodes(3)
    print(G.v)
    print(MST(G))
    print(getMinDict(MST(G)))

    #t = time()
    #m = MST(G1)
    #print(time() - t)    

foo()
