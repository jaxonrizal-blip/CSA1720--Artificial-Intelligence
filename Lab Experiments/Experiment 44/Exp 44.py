import cv2
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from tkinter import Tk, filedialog

# Step 1: Select an image
root = Tk()
root.withdraw()

image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[
        ("Image Files", "*.jpg *.jpeg *.png")
    ]
)

if not image_path:
    print("No image selected!")
    exit()

# Step 2: Read the image
image = cv2.imread(image_path)

if image is None:
    print("Unable to load image!")
    exit()

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Resize image for faster processing
image = cv2.resize(image, (200, 200))

# Step 3: Convert image into pixel data
pixels = image.reshape((-1, 3))

# Step 4: Apply K-Means clustering
k = 3

kmeans = KMeans(
    n_clusters=k,
    random_state=42,
    n_init=10
)

labels = kmeans.fit_predict(pixels)

# Step 5: Replace pixels with cluster colors
centers = np.uint8(kmeans.cluster_centers_)

segmented_image = centers[labels]
segmented_image = segmented_image.reshape(image.shape)

# Step 6: Display original and segmented images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(segmented_image)
plt.title("Segmented Image (K=3)")
plt.axis("off")

plt.tight_layout()
plt.show()

# Step 7: Save segmented image
segmented_image = cv2.cvtColor(
    segmented_image, cv2.COLOR_RGB2BGR
)

cv2.imwrite("segmented_image.jpg", segmented_image)

print("Image Segmentation Completed Successfully!")
print("Number of Clusters:", k)
print("Output saved as segmented_image.jpg")
