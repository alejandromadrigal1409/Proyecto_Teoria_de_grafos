import networkx as nx
import matplotlib.pyplot as plt

def grafoRegular(n, r):

    if (n * r) % 2 != 0:
            raise ValueError("n*r debe ser par")

    G = nx.Graph()
    G.add_nodes_from(range(n))

    # conexión tipo anillo base
    for i in range(n):
        G.add_edge(i, (i + 1) % n)

    for i in range(n):
         for j in range(r):
              aux = (i+j+2)%n
              print(aux)
              if not G.has_edge(i,aux) and not G.has_edge(aux,i) and aux != i:
                G.add_edge(i,aux)

    return G

G = grafoRegular(4, 2)
nx.draw(G, node_size=80, with_labels=True)
print(G.edges())
plt.show()