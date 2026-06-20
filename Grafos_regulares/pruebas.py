import os
import networkx as nx
import matplotlib.pyplot as plt
from Grafo_r_regular import grafoRegular

# Crear carpeta si no existe
os.makedirs("resultados", exist_ok=True)


pruebas = [
    (2, 1),
    (3, 2),
    (4, 1),
    (4, 2),
    (4, 3),
    (5, 2),
    (5, 4),
    (6, 1),
    (6, 2),
    (6, 3),
    (6, 4),
    (6, 5),
    (7, 2),
    (7, 4),
    (7, 6),
    (8, 2),
    (8, 3),
    (8, 4),
    (8, 6),
    (8, 7),
    (10, 2),
    (10, 3),
    (10, 4),
    (10, 5),
    (12, 3),
    (12, 5),
    (14, 4),
    (15, 4),
    (16, 6),
    (20, 10)
]

# Experimentos con diferentes valore de n y r
for n, r in pruebas:
    G = grafoRegular(n, r)

    # Dibujar
    nx.draw_circular(G, with_labels=True)

    # Guardar imagen
    plt.savefig(f"resultados/Grafo_{r}_regular_orden_{n}", dpi=300, bbox_inches="tight")
    plt.close()