import numpy as np
import matplotlib.pyplot as plt

Arr = np.zeros((11, 11))
for i in range(11):
    for j in range(11):
        if i != 0 or j != 0:
            Arr[i, j] = (i**0.5 + j**0.5) / 0.3 / (i + j)

fig, ax = plt.subplots(figsize=(6, 6))
im = plt.imshow(Arr, alpha=1)
plt.xticks(np.arange(0, 10, step=1))

fig.colorbar(im, orientation="vertical", pad=0.2)
plt.title("Formula assessment model for class assessment")

plt.pause(100)
