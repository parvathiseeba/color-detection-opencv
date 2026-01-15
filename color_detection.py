import cv2
import numpy as np
from sklearn.cluster import KMeans
from google.colab import files
import matplotlib.pyplot as plt

# --- Upload Image ---
uploaded = files.upload()
filename = list(uploaded.keys())[0]

# --- Read & Preprocess Image ---
image = cv2.imread(filename)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (400, 400))  # optional resizing
pixels = image.reshape((-1, 3))

# --- K-Means Clustering ---
k = 5  # number of dominant colors
kmeans = KMeans(n_clusters=k, random_state=42)
labels = kmeans.fit_predict(pixels)
colors = kmeans.cluster_centers_

# --- Color Ranking by Frequency ---
counts = np.bincount(labels)
sorted_idx = np.argsort(counts)[::-1]  # most frequent first
colors = colors[sorted_idx]
counts = counts[sorted_idx]
percentages = counts / sum(counts)

# --- Display Image & Dominant Colors ---
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.imshow(image)
plt.axis('off')
plt.title("Original Image")

plt.subplot(1,2,2)
for i, color in enumerate(colors):
    plt.bar(i, 1, color=color/255.0)
plt.xticks([])
plt.yticks([])
plt.title("Dominant Colors")
plt.show()

# --- Print Dominant Colors & Percentages ---
print("Dominant Colors (RGB) and % in image:")
for i, (color, perc) in enumerate(zip(colors.astype(int), percentages)):
    print(f"{i+1}. {color} - {perc*100:.2f}%")
