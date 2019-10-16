from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s):
        q=[]
        vis=[0]*(len(self.graph))
        q.append(s)
        vis[s]=1
        while(q):
            s=q.pop(0)
            print(s)
            for i in self.graph[s]:
                if vis[i]==0:
                    q.append(i)
                    vis[i]=1
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.bfs(2)
