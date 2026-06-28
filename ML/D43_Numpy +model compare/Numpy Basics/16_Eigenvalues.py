import numpy as np

matrix = np.array([
    [1, 2],
    [3, 4]
])

# Find eigenvalues and eigenvectors
values, vectors = np.linalg.eig(matrix)

print("Eigenvalues:")
print(values)

print("\nEigenvectors:")
print(vectors)


#output
# Eigenvalues:
# [-0.37228132  5.37228132]           # det(A-λ)=0 formula of eigen values

# Eigenvectors:
# [[-0.82456484 -0.41597356]         #(A−λI)v=0 formula gets eigenvector
#  [ 0.56576746 -0.90937671]]        #apply this formulla we get x,y then Z=sqrt(X^2+Y^2)
                                     #then X/Z ,Y/Z  this is eigenvectors 
                                     #NumPy changes vector length to 1.This is called NORMALIZATION.