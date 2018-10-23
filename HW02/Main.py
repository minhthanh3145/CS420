# @Author: Thành, Tô - 1551032
# Course: CS420
# Homework: 02

import sys 
from collections import defaultdict 
import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
class Graph: 
  
    # Constructor 
    def __init__(self, start, goal, numberOfNodes):
        # We need to use numberOfNodes
        # because the size of the adjacency matrix
        # depends on whether a node is completely isolated 
        # if there exists N such nodes:
        # len(self.graph) + N = self.numberOfNodes
        self.numberOfNodes = numberOfNodes
        self.graph = defaultdict(list)
        self.cost = defaultdict(list)
        self.start = start
        self.goal = goal

    def addEdge(self, u, v, c):
        self.graph[u].append(v)
        self.cost[u, v] = c

    def BFS(self, start, goal):
        visited = [False] * (self.numberOfNodes)
        queue = []
        queue.append(start) 
        self.BFS_expandedNodes = []
        self.BFS_parent = defaultdict(list)
        visited[start] = True 
        while queue:
            currentNode = queue.pop(0)
            self.BFS_expandedNodes.append(currentNode)
            if currentNode == goal:
                return;
            for i in self.graph[currentNode]:
                if visited[i] == False:
                    self.BFS_parent[i] = currentNode;
                    queue.append(i)
                    visited[i] = True
                    
    
    def BFS_getExpandedNodes(self):
        return self.BFS_expandedNodes
        
    def BFS_getPath(self):
        path = []
        current = self.goal
        path.insert(0, current)
        while self.BFS_parent[current] != []:
            path.insert(0, self.BFS_parent[current])
            current = self.BFS_parent[current]   
                
        if len(path) == 1:
            return 'No path is found'        
        return path
        

    def DFS_goInDepth(self, current, goal, visited): 
        visited[current]= True
        self.DFS_expandedNodes.append(current)
        if current == goal:
            return True
        for i in self.graph[current]:
            if visited[i] == False:
                self.DFS_parent[i] = current
                if self.DFS_goInDepth(i, goal, visited) == True:
                    return True


    def DFS(self, start, goal):
        self.DFS_parent = defaultdict(list)
        self.DFS_expandedNodes = []
        visited = [False]*(self.numberOfNodes)
        self.DFS_goInDepth(start, goal, visited)
    
    def DFS_getExpandedNodes(self):
        return self.DFS_expandedNodes
    
    def DFS_getPath(self):
        path = []
        current = self.goal
        path.insert(0, current)
        while self.DFS_parent[current] != []:
            path.insert(0, self.DFS_parent[current])
            current = self.DFS_parent[current]
            
        if len(path) == 1:
            return 'No path is found'
        
        return path
    
        
    def UFS(self, start, goal):
        queue = PriorityQueue()
        queue.put(start, 0)
        self.UFS_expandedNodes = []
        self.UFS_parent = defaultdict(list)
        costSoFar = defaultdict(list)
        costSoFar[start] = 0
        
        while not queue.empty():
            current = queue.get()
            self.UFS_expandedNodes.append(current)            
            if current == goal:
                break
            for i in self.graph[current]:
                new_cost = costSoFar[current] + self.cost[current, i]
                if i not in costSoFar or new_cost < costSoFar[i]:
                    # A star with constant costSoFar
                    costSoFar[i] = 0
                    priority = new_cost
                    queue.put(i, priority)
                self.UFS_parent[i] = current
        
    def UFS_getExpandedNodes(self):
        return self.UFS_expandedNodes
        
    def UFS_getPath(self):
        path = []
        current = self.goal
        path.insert(0, current)
        while self.UFS_parent[current] != []:
            path.insert(0, self.UFS_parent[current])
            current = self.UFS_parent[current]
            
        if len(path) == 1:
            return 'No path is found'
        
        return path
    
    
    
# Utility to parse input file into an array
def readfile(fileName):
    with open(fileName) as f:
        content = f.readlines()

    return content

def writefile(fileName, res):
    outfile = open(fileName, "w")
    outfile.writelines(["%s\n" % item  for item in res])


if __name__ == '__main__':
    
    # inputFile = str(sys.argv[1])
    # outputFile = str(sys.argv[2])
    
    content = readfile("input.txt")
    # Parse necessary parameters
    try:
        numberOfNodes = int(content[0])
        source = int(content[1].split(' ')[0])
        destination = int(content[1].split(' ')[1])
        strategy = int(content[1].split(' ')[2])
        
        numberOfNodes = len(content[2:])        
        # Initialize an adjacency graph from parsed information
        g = Graph(source, destination, numberOfNodes)
        i = 0
        for i, row in enumerate(content[2:]):
            for j, digit in enumerate(row.split(' ')):
                if(int(digit) != 0):
                    g.addEdge(i, j, int(digit))
    except:
        print 'Unexpected error: ', sys.exc_info()[0]
        raise
    
    res = []
    # Output by mapping integer to string and join them by spaces
    if strategy == 0:
        g.BFS(source, destination)
        res.append(" ".join(map(str, g.BFS_getExpandedNodes())))
        res.append(" ".join(map(str, g.BFS_getPath())))
    elif strategy == 1:
        g.DFS(source, destination)
        res.append(" ".join(map(str, g.DFS_getExpandedNodes())))
        res.append(" ".join(map(str, g.DFS_getPath())))
    elif strategy == 2:
        g.UFS(source, destination)
        res.append(" ".join(map(str, g.UFS_getExpandedNodes())))
        res.append(" ".join(map(str, g.UFS_getPath())))
    
    writefile("output.txt", res)
    pass