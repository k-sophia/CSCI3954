"""
Test driver for Program 50
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.datasets import load_sample_image
import p50


china = load_sample_image("china.jpg") #from sample image
china_4col = p50.coloring(china)
fig, ax = plt.subplots(1, 2, figsize=(16, 6),
                       subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(china)
ax[0].set_title('Original Image', size=16)
ax[1].imshow(china_4col)
ax[1].set_title('4-color Image', size=16);
# Expected plot 4color.png
plt.show()