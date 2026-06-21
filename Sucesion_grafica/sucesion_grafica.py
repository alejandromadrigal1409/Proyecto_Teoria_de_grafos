import networkx as nx

def sucesionGrafica(s):
    G = nx.Graph()
    n = len(s)

    # (identificador del nodo, grado)
    vertices = [(i, s[i]) for i in range(n)]
    G.add_nodes_from(range(n))

    while True:

        # ordena los vértices por grado de mayor a menor
        vertices.sort(key=lambda x: x[1], reverse=True)

        # caso base: todos los grados son 0
        if all(x[1] == 0 for x in vertices):
            return G

        # selecciona y elimina el nodo con mayor grado
        v, d = vertices.pop(0)

        # no puede haber un grado mayor que el número de nodos restantes
        if d > len(vertices):
            return False

        for i in range(d):
            u, deg = vertices[i]

            # conecta el nodo con mayor grado con los d nodos de mayor grado restantes
            G.add_edge(v, u)

            # reduce en 1 el grado de los nodos restantes
            vertices[i] = (u, deg - 1)

            # verifica si hay algún grado negativo
            if vertices[i][1] < 0:
                return False