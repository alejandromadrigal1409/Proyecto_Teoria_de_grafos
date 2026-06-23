import networkx as nx

def primAlgorithm(G):

    if len(G.nodes) == 0:
        return nx.Graph()

    T = nx.Graph()

    start = list(G.nodes)[0]

    visited = {start}
    T.add_node(start)

    while len(visited) < len(G.nodes):

        minWeight = float("inf")
        edgeStart = None
        edgeEnd = None

        for u in visited:
            for v, attrs in G[u].items():

                weight = attrs["weight"]

                if v not in visited and weight < minWeight:
                    minWeight = weight
                    edgeStart = u
                    edgeEnd = v

        if edgeEnd is None:
            raise ValueError("El grafo no es conexo")

        T.add_edge(edgeStart, edgeEnd, weight=minWeight)
        visited.add(edgeEnd)

    return T