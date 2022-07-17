from http.client import NotConnected


class graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

    # Get the keys of the dictionary
    def getvertices(self):
        return list(self.gdict.keys())


class graph2:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
    # Find the distinct list of edges

    def findedges(self):
        edgename = []
        for i in self.gdict:
            for j in self.gdict[i]:
                if {j, i} not in edgename:
                    edgename.append({i, j})
        return edgename

    # Create the dictionary with graph element
graph_element = {
    "a": ["b", "c"],
    "b": ["a", "d"],
    "c": ["a", "d"],
    "d": ["e"],
    "e": ["d"]
}

# Print the graph
g = graph(graph_element)
g2 = graph2(graph_element)
print(g2.edges())
print(graph_element)
print(g.getvertices())
