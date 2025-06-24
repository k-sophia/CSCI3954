"""
Resources: jakevdp.hithub.io for MiniBatchKMeans
"""

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import MiniBatchKMeans

def coloring(img, n_clusters = 4, random_state=5):
    temp_img = img/255.0
    temp_img = temp_img.reshape(427*640, 3)
    
    kmeans = MiniBatchKMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(temp_img)
    new_colors = kmeans.cluster_centers_[kmeans.predict(temp_img)]
    img_color = new_colors.reshape(img.shape)

    return img_color