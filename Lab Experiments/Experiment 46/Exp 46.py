from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog
import os

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

# Step 2: Load local YOLO model
print("Loading YOLO model...")

model_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "yolo11n.pt"
)

if not os.path.exists(model_path):
    print("Error: yolo11n.pt not found!")
    print("Place the model in the same folder as this Python file.")
    exit()

model = YOLO(model_path)

# Step 3: Perform object detection
print("Detecting objects...")

results = model.predict(
    source=image_path,
    conf=0.25
)

# Step 4: Get detection results
result = results[0]

print("\nDetected Objects:")

if result.boxes is not None and len(result.boxes) > 0:

    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        object_name = model.names[class_id]

        print(
            object_name,
            "- Confidence:",
            round(confidence * 100, 2),
            "%"
        )

else:
    print("No objects detected.")

# Step 5: Draw bounding boxes
annotated_image = result.plot()

# Convert BGR to RGB
annotated_image = cv2.cvtColor(
    annotated_image,
    cv2.COLOR_BGR2RGB
)

# Step 6: Display output
plt.figure(figsize=(10, 7))

plt.imshow(annotated_image)
plt.title("YOLO Object Detection")
plt.axis("off")

plt.show()

# Step 7: Save output image
output_path = "detected_objects.jpg"

cv2.imwrite(
    output_path,
    cv2.cvtColor(annotated_image, cv2.COLOR_RGB2BGR)
)

print("\nOutput saved as:", output_path)
print("Object Detection Completed Successfully!")
