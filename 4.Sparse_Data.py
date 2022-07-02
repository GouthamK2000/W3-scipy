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



#Case-2-count_nonzero()
import numpy as np
from scipy.sparse import csr_matrix

arr=np.array([[3,0,0],[6,1,0],[0,0,0]])
print(csr_matrix(arr).count_nonzero())  #count_nonzero(), retuns the number of non zero elements in the given array.

#Case-3- printing all the digits without zeroes

import numpy as np
from scipy.sparse import csr_matrix

arr= np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
print(csr_matrix(arr).data) #.data ensures only the non zero elemnts are printed

#Case-4-Eliminating duplicates

import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.sum_duplicates()   #.sum_duplicates eliminates all the duplicates

print(mat)