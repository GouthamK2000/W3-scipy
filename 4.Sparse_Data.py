# What is Sparse Data
# Sparse data is data that has mostly unused elements (elements that don't carry any information ).

# It can be an array like this one:

# [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0]

# Sparse Data: is a data set where most of the item values are zero.

# Dense Array: is the opposite of a sparse array: most of the values are not zero.


# How to Work With Sparse Data
# SciPy has a module, scipy.sparse that provides functions to deal with sparse data.

# There are primarily two types of sparse matrices that we use:

# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.

# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products

# We will use the CSR matrix in this tutorial.


#Case-1- CSR matrix

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))

#Output:
#   (0, 5)	1
#   (0, 6)	1
#   (0, 8)	2


