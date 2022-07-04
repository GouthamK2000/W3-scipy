# Working with Graphs
# Graphs are an essential data structure.

# SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.

# Adjacency Matrix
# Adjacency matrix is a nxn matrix where n is the number of elements in a graph.

# And the values represents the connection between the elements.

# Example:

# Diagram-https://www.w3schools.com/python/scipy/scipy_graphs.php
# For a graph like this, with elements A, B and C, the connections are:

# A & B are connected with weight 1.

# A & C are connected with weight 2.

# C & B is not connected.

# The Adjency Matrix would look like this:


#       A B C
#    A:[0 1 2]  
#    B:[1 0 0]
#    C:[2 0 0]

# Below follows some of the most used methods for working with adjacency matrices.


#Connected components

import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr=csr_matrix(arr)
print(connected_components(newarr))