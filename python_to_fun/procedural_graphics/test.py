import numpy as np
import matplotlib.pyplot as plt
from  matplotlib.colors import ListedColormap

matrix = np.random.randint(0, 2, (5, 5))
print(matrix)
plt.matshow(matrix, cmap=ListedColormap(['k','w']))
plt.show()

