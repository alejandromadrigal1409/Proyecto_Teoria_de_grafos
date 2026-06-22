import networkx as nx

def kruskalTree(G):

    T = nx.Graph()

    # Diccionario que simula una estructura de conjuntos disjuntos
    # Inicialmente cada nodo pertenece a su propio conjunto
    # El valor asociado a cada nodo es el nombre de su conjunto
    conjuntos = {}

    for v in G.nodes:
        conjuntos[v] = v

    def find(u):
        # Devuelve el nombre actual del conjunto del nodo u
        return conjuntos[u]

    def union(u, v):

        nameSetOfU = find(u)
        nameSetOfV = find(v)

        # Une dos conjuntos haciendo que todos los nodos
        # del conjunto de v tengan el nombre del conjunto de u
        for node in conjuntos:
            if conjuntos[node] == nameSetOfV:
                conjuntos[node] = nameSetOfU

    # Ordena las aristas por peso en orden creciente
    edges = sorted(G.edges(data=True), key=lambda e: e[2]["weight"])

    for u, v, data in edges:

        # Solo se agrega la arista si conecta dos componentes distintas
        if find(u) != find(v):

            # Agrega la arista al árbol de expansión mínima
            T.add_edge(u, v, weight=data["weight"])

            union(u, v)

            # Kruskal termina cuando el árbol tiene n-1 aristas
            if len(T.edges) == len(G.nodes) - 1:
                break

    return T


