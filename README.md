# Teoría de Grafos

Este repositorio contiene implementaciones en Python de algoritmos clásicos de teoría de grafos. Para la generación y manipulación de grafos se utiliza la librería **NetworkX**, y para la visualización de resultados, **Matplotlib**.

Los algoritmos implementados son:

- Generación de grafos r-regulares de orden n.
- Generación de un grafo a partir de una sucesión gráfica.
- Kruskal.
- Kruskal Inverso (Reverse Delete).
- Prim.

Cada algoritmo cuenta con una carpeta de resultados que incluye capturas del funcionamiento y los resultados obtenidos.

## Instalación

Para ejecutar el proyecto, instala las dependencias necesarias con:

```bash
pip install networkx matplotlib
```

## Metodología de desarrollo

Cada algoritmo fue implementado de forma modular, aprovechando las estructuras de grafos que ofrece NetworkX. A continuación se describe brevemente cada uno:

### Generación de grafos r-regulares de orden n

Construye grafos en los que todos los `n` vértices tienen el mismo grado `r`, verificando previamente la factibilidad de la construcción (es decir, que `r < n` y que `r * n` sea par).

![Grafo 10-regular de orden 20](Grafos_regulares/resultados/Grafo_10_regular_orden_20.png)

### Generación de un grafo a partir de una sucesión gráfica

Determina si una secuencia de grados es válida y construye un grafo simple que la satisface.

![Grafo generado a partir de la sucesión 5,5,5,5,2,2,2,2,1,1](Sucesion_grafica/resultados/Grafo_sucesion_5_5_5_5_2_2_2_2_1_1.png)

### Kruskal

Obtiene un árbol generador mínimo seleccionando iterativamente las aristas de menor peso, evitando la formación de ciclos.

![Árbol generador mínimo — Kruskal (experimento 3)](Kruskal/resultados/Kruskal_MST_experimento_3.png)

### Kruskal Inverso (Reverse Delete)

Parte del grafo completo y elimina aristas de mayor peso, siempre que su eliminación no desconecte el grafo, hasta obtener un árbol generador mínimo.

![Árbol generador mínimo — Reverse Delete (experimento 3)](Reverse_Delete/resultados/Reverse_Delete_MST_experimento_3.png)

### Prim

Construye un árbol generador mínimo expandiendo progresivamente un conjunto de vértices, añadiendo en cada paso la arista de menor peso que conecta un vértice ya incluido con uno que aún no lo está.

![Árbol generador mínimo — Prim (experimento 4)](Prim/resultados/Prim_MST_experimento_4.png)

Autor

Alejandro Madrigal
