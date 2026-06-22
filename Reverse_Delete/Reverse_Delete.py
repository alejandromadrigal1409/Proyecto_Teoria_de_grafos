import networkx as nx

def dfs(adjList, u, visited):
  visited[u] = True
  for v in adjList[u]:
    if not visited[v]:
      dfs(adjList, v, visited)
  return visited

def constructAdjList(G, edge):
    # Inicializar lista de adyacencia
    adjacencies = {node: [] for node in G.nodes()}

    # Agregar todas las aristas excepto la indicada
    for u, v in G.edges():
        if (u, v) == edge or (v, u) == edge:
            continue

        adjacencies[u].append(v)
        adjacencies[v].append(u)

    return adjacencies

def isBridge(G, edge):
  # probar si la arista (u, v) es un puente
  # construir un grafo sin la arista
  adjList = constructAdjList(G, edge)

  u, v = edge # extremos de la arista que si quiere probar si es puente
  # diccionario que indica cuales nodos de todo el grafo son alcanzables desde u
  visited = {node: False for node in G.nodes}

  reachableNodes = dfs(adjList, u, visited)
  # si no se puede alcanzar a la arista v desde u, entonces edge es un puente
  return not reachableNodes[v]

def ReverseDeleteAlgorithm(G):
  T = G.copy()
  edges = list(T.edges(data=True))
  edges.sort(reverse = True, key = lambda e: e[2]["weight"])

  for edge in edges:
    if not isBridge(T, edge[:-1]):
      T.remove_edge(edge[0], edge[1])

  return T