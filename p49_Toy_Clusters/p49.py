"""
Name: Kelly Camacho
Email: kelly.camacho02@myhunter.cuny.edu
Resources: jakevdp.github.io about kmeans
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.manifold import MDS
from sklearn.manifold import TSNE
from sklearn.metrics import accuracy_score
from scipy.stats import mode

def clusterDemo(toy_dataset, n_components = 2, n_clusters = 3, method = "none", random_state=0):
    data = toy_dataset.data

    if method == 'TSNE':
        tsne = TSNE(n_components=n_components, random_state=random_state)
        data = tsne.fit_transform(toy_dataset.data) 

    if method == 'MDS':
        mds = MDS(random_state=random_state, n_components=n_components)
        data = mds.fit_transform(toy_dataset.data)

    if method == 'none':
        data = toy_dataset.data


    # Compute the clusters
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    clusters = kmeans.fit_predict(data)

    # Permute the labels
    labels = np.zeros_like(clusters)
    for i in range(n_clusters):
        mask = (clusters == i)
        labels[mask] = mode(toy_dataset.target[mask])[0]

    # Compute the accuracy
    return accuracy_score(toy_dataset.target, labels)