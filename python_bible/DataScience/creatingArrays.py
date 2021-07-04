import numpy as np

a = np.array([10, 20, 30])
b = np.array([1, 77, 2, 3])

print(a[0])
print(b[3])

# MULTI-DIMENSIONAL ARRAYS

c = np.array([[10, 20, 30], [40, 50, 60]])

print(c)
print(c[1][2])

e = np.array([
    [
        [10, 20, 30, 40], [8, 8, 2, 1], [1, 1, 1, 2]
    ],
    [
        [9, 9, 2, 39], [1, 2, 3, 3], [0, 0, 3, 2]
    ], [
        [12, 33, 22, 1], [22, 1, 22, 2], [0, 2, 3, 1]
    ]
], dtype=float)

print(e)

# FULL FUNCTION to generate values for array
f = np.full((3, 5, 4), 7)
print(f)

print(np.zeros((5, 3, 4)))
print(np.ones((2, 3, 4, 2)))
g = np.empty((5, 1, 3, 6, 4))
print("\n", g)
print(g.ndim, g.size)

print(np.random.random((2, 3)))
print(np.arange(10, 50, 5))
print("\n", np.linspace(0, 100, 11))
