import os
import networkx as nx
import matplotlib.pyplot as plt
from Reverse_Delete import ReverseDeleteAlgorithm
import random

os.makedirs("resultados", exist_ok=True)

tests = [
    (4, 0.9),
    (5, 0.9),
    (6, 0.85),
    (8, 0.8),
    (10, 0.8),
    (12, 0.75),
    (10, 0.85),
    (12, 0.85),
    (15, 0.8),
    (10, 0.9),
    (12, 0.9),
    (15, 0.9),
    (8, 0.95),
    (10, 0.95),
    (12, 0.95),
    (20, 0.75),
    (20, 0.8),
    (25, 0.75),
    (20, 0.85),
    (25, 0.85),
    (30, 0.8),
    (30, 0.9),
    (30, 0.95),
    (40, 0.85),
    (25, 0.95),
    (30, 0.95),
    (15, 0.75),
    (20, 0.75),
    (18, 0.8),
    (22, 0.85),
]


for i, (n, p) in enumerate(tests):

    G = nx.erdos_renyi_graph(n, p)

    for u, v in G.edges():
        G[u][v]["weight"] = random.randint(1, 100)

    T = ReverseDeleteAlgorithm(G)

    # Crear subplots
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Posiciones de los nodos (las mismas para ambos gráficos)
    pos = nx.spring_layout(G, seed=23)

    # Etiquetas de pesos
    labels_G = nx.get_edge_attributes(G, 'weight')
    labels_mst = nx.get_edge_attributes(T, 'weight')

    # Grafo original
    nx.draw(
        G,
        pos,
        ax=ax[0],
        with_labels=True,
        node_size=150
    )
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=labels_G,
        ax=ax[0]
    )
    ax[0].set_title("Grafo original")


    # MST
    nx.draw(
        T,
        pos,
        ax=ax[1],
        with_labels=True,
        node_size=150
    )

    nx.draw_networkx_edge_labels(
        T,
        pos,
        edge_labels=labels_mst,
        ax=ax[1]
    )

    ax[1].set_title("Árbol de expansión mínima (Kruskal)")

    nombre = f"resultados/Kruskal_MST_experimento_{i + 1}.png"

    plt.savefig(
        nombre, 
        dpi=300, 
        bbox_inches="tight"
    )

    plt.close()
