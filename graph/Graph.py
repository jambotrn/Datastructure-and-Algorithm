

class Graph:
    def __init__(self):
        self.numberOfNode= 0
        self.adjacentList = {}

    def addVertex(self,node):
        self.adjacentList[node] = []
        self.numberOfNode += 1

    def addEdge(self, node1, node2):
        #undirected Graph
        
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1) 

    def showConnections(self):
        allnode = self.adjacentList.keys()
        for node in allnode:
            nodeConections = self.adjacentList[node]
            connections = ''
            for vertex in nodeConections:
                connections += vertex + " "
            print(node + " --> " + connections)

graphObj = Graph()

graphObj.addVertex('0')
graphObj.addVertex('1')
graphObj.addVertex('2')
graphObj.addVertex('3')
graphObj.addVertex('4')
graphObj.addVertex('5')
graphObj.addVertex('6')

graphObj.addEdge('3', '1')
graphObj.addEdge('3', '4')
graphObj.addEdge('4', '2')
graphObj.addEdge('4', '5')
graphObj.addEdge('1', '2')
graphObj.addEdge('1', '0')
graphObj.addEdge('0', '2')
graphObj.addEdge('6', '5')

graphObj.showConnections()