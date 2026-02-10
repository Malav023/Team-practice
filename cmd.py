import numpy as np
a = np.random.randint(1, size=(5,5))
a[0]=1
a[4]=1
a[:, 0]=1
a[:, 4]=1
a[2,2] = 9
print(a)