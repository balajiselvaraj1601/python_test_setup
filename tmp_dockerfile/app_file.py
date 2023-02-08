import numpy as np
from sklearn.model_selection import train_test_split
X, Y = np.arange(10).reshape((5, 2)), range(5)

print("----------------------------------------------------------")
print(f"Value of X:  {X}")
print(f"Value of Y:  {Y}")

for i in range(0,10):
    print(f"--------> {i}")