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
    (8, 4),
    (8, 6),
    (10, 2),
    (10, 4),
    (10, 5),
    (14, 4),
    (15, 4),
    (16, 6),
    (20, 10),
    (5, 3),
    (7, 3),
    (7, 5),
    (8, 3),
    (8, 7),
    (10, 3),
    (12, 3),
    (12, 5),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (5, 6),
    (4, 7),
    (1, 0),  
    (0, 0),  
    (2, 3),  
    (10, 15) 
]

for n, r in pruebas:
    try:
        G = grafoRegular(n, r)

        nx.draw_circular(G)

        plt.title(f"Grafo {r}-regular de orden {n}")

        nombre = f"resultados/Grafo_{r}_regular_orden_{n}.png"
        plt.savefig(
            nombre,
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    except ValueError as e:
        print(f"({n}, {r}): {e}")