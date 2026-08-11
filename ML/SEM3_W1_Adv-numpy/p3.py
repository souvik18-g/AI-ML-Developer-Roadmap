 #Convert a 1D array into 2D.

import numpy as np
x = np.array([1, 2, 3,4,5,6,7,8,9])

print(x.shape)

y=np.expand_dims(x,axis=0)
print(y)
print(y.shape)
z=np.expand_dims(x,axis=1)
print(z)
print(z.shape)

#Convert (9,1) back to (9,).
a=np.squeeze(z)
print(a.shape)