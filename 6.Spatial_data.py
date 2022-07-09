# Working with Spatial Data
# Spatial data refers to data that is represented in a geometric space.

# E.g. points on a coordinate system.

# We deal with spatial data problems on many tasks.

# E.g. finding if a point is inside a boundary or not.

# SciPy provides us with the module scipy.spatial, which has functions for working with spatial data.



# Triangulation
# A Triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon.

# A Triangulation with points means creating surface composed triangles in which all of the given points are on at least one vertex of any triangle in the surface.

# One method to generate these triangulations through points is the Delaunay() Triangulation.

import numpy as np
from scipy.spatial import Delayunay
import matplotlib.pyplot as plt

points=([[2,4],[45,67],[3,4],[78,90],[9,8]])
simplices=Delayunay(points).simplices
plt.triplot(points[:, 0], points[:, 1], simplices)
plt.scatter(points[:, 0], points[:, 1], color='r')

plt.show()

#Outputs:  A polygon divided into triangles.
