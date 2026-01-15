import cv2
import numpy as np
from sklearn.cluster import KMeans

# Read image
image = cv2.imread("image.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Reshape image
pixels = image.reshape((-1, 3))

# Apply K-Means
kmeans = KMeans(n_clusters=3)
kmeans.fit(pixels)

# Get dominant colors
colors = kmeans.cluster_centers_

print("Dominant Colors:")
for color in colors:
    print(color.astype(int))
