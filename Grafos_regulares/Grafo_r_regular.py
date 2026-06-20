import os
import networkx as nx
import matplotlib.pyplot as plt

def grafoRegular(n, r):

    if n <= r:
        raise ValueError("n debe ser mayor que r para un grafo simple")
    
    if (n * r) % 2 != 0:
        raise ValueError("n*r debe ser par")
    
    G = nx.Graph()
    G.add_nodes_from(range(n))

    # Conectar a los r/2 vecinos de cada nodo
    k = r // 2
    for i in range(n):
        for j in range(1, k + 1):
            G.add_edge(i, (i + j) % n)
    
    # Conecta al nodo opuesto para r impar
    if r % 2 != 0:
        for i in range(n // 2):
            G.add_edge(i, i + (n // 2))

    return G

