import networkx as nx

def primAlgorithm(G):
  T = nx.Graph()
  visitedComponent = set()

  # crear lista de adyacencias del grafo
  adjList = {node: {} for node in G.nodes}
  for edge in G.edges:
    adjList[edge[0]][edge[1]] = G[edge[0]][edge[1]]["weight"]
    adjList[edge[1]][edge[0]] = G[edge[1]][edge[0]]["weight"]

  # seleccionar un nodo
  u = list(G.nodes)[0]
  visitedComponent.add(u)

  while len(visitedComponent) < len(G.nodes):
    aux = {}
    for u in visitedComponent:
      aux[u] = adjList[u]

    minWeight = float('inf')
    minOut = None
    edgeStart = None
    for i in aux:
      for node, weight in aux[i].items():
        if weight < minWeight and node not in visitedComponent:
          minWeight = weight
          minOut = node
          edgeStart = i
    T.add_edge(edgeStart, minOut, weight=minWeight)
  
    visitedComponent.add(minOut)
    
  return T
