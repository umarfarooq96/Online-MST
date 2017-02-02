from random import *
from time import time
from math import sqrt
import sys


class point:
    
    def __init__(self):
        
        self.x = random()
        self.y = random()

def dist(a,b):
    
    d = sqrt((a.x-b.x)**2 + (a.y-b.y)**2)
    
    return d

def makeEdges(V, origin):
    
    E = []
    for v in V:
            if(v != origin):

                E += [(origin, v, dist(origin, v))]
    return E

def MST(V):
    
    unvisited = [point() for i in range(V)]    
    nv = unvisited[0]
    unvisited = unvisited[1:]
    edges = []
    mst = []
    seen = {}
    
    for i in unvisited: #no V has been seen 
        seen[i] = 0
        
    for i in range(V-1):
        
        edges = sortedEdges(edges + makeEdges(unvisited, nv)) #all now visable edges
        mst += [edges[0]] #pick smallest edge
        
        edges = edges[1:] #remove the edge we picked
            
        nv = mst[-1][1] #new V that has now been seen    
        seen[nv] = 1
        
        unvisited.remove(nv) #remove newly found v
        edges = [edges for e in edges if seen[e[1]]] #remove all other edges to nv
    
    return mst
    
def getWeight(e):
        
    return e[2]

def sortedEdges(E):
        return sorted(E, key=getWeight)
    

def circleMST(V):
    m = MST(V)
    s = 0
    for i in m:
        s += i[2]
        
    return s
    
    

argv = sys.argv
print(circleMST(int(argv[1])))
