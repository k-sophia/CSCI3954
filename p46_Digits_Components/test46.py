"""
Name:  Katherine St. John
Email: katherine.stjohn@hunter.cuny.edu
Resources:  Used textbook, scikit-learn.org (recognizing handwritten digits),
    and https://jakevdp.github.io/PythonDataScienceHandbook/
"""

import pandas as pd
import numpy as np
#import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt

#Contains the approxDigits()
import p46
#import student

#Using the digits data set from sklearn:
from sklearn import datasets
digits = datasets.load_digits()

#Using the PCA from sklearn:
from sklearn.decomposition import PCA

#Helper function that reshapes and plots digit data:
def showDigit(digit,title = "",filename = ""):
    plt.imshow(digit.reshape(8,8),
                cmap='binary', interpolation='nearest',clim=(0, 16))
    plt.title(title)
    if filename == "":
        plt.show()
    else:
        plt.savefig(filename)

#Test run with digits.data[10] and 8 components
sampleNum = 0
numComps = 8
# showDigit(digits.data[sampleNum], f"digits[{sampleNum}] (actual)" )

#Run PCA and store result in Xproj:
pca = PCA()
Xproj = pca.fit_transform(digits.data)

showDigit(pca.mean_, f"Mean for digits")

approxAnswer = p46.approxDigits(numComps,Xproj[sampleNum], pca.mean_, pca.components_)

showDigit(approxAnswer, f"mean + {numComps} components for digits[{sampleNum}]")
from mpl_toolkits.axes_grid1 import ImageGrid

fig = plt.figure(figsize=(25,5))
grid = ImageGrid(fig, 111,  # similar to subplot(111)
                 nrows_ncols=(1, 12)
                 )

print(sum(p46.approxDigits(2,Xproj[sampleNum], pca.mean_, pca.components_)
    -p46.approxDigits(64,Xproj[sampleNum], pca.mean_, pca.components_)))

showDigit(pca.mean_, f"Mean for digits")

for ax, i in zip(grid, range(12)):
    ax.get_xaxis().set_ticks([])
    ax.get_yaxis().set_ticks([]
    )
    if i == 0:
        ax.imshow(digits.data[sampleNum].reshape(8,8),
            cmap='binary', interpolation='nearest',clim=(0, 16))
        ax.set_title("Original", fontsize=10)
    elif i == 1:
        ax.imshow(pca.mean_.reshape(8,8),
            cmap='binary', interpolation='nearest',clim=(0, 16))
        ax.set_title("Mean", fontsize=10)
    else:
        appproxAnswer = p46.approxDigits(i-1,Xproj[sampleNum], pca.mean_, pca.components_)
        ax.imshow(approxAnswer.reshape(8,8),
                cmap='binary', interpolation='nearest',clim=(0, 16))
        ax.set_title(f"+c[{i-2}]*i[{i-2}]",fontsize=10)

'''
for i in range(10):
    ax = fig.add_subplot(i+1,1,i+1)
    ax.imshow(digits.data[0].reshape(8,8),
        cmap='binary', interpolation='nearest',clim=(0, 16))
    ax.set_title("Original")
'''

plt.show()
