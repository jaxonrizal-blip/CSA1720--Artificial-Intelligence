from deepface import DeepFace
import os

# Enter image paths
image1 = input("Enter first image path: ").strip().strip('"')
image2 = input("Enter second image path: ").strip().strip('"')

if not os.path.isfile(image1) or not os.path.isfile(image2):
    print("Error: Image file not found!")
else:
    try:
        print("\nFace Recognition Started...")

        result = DeepFace.verify(
            img1_path=image1,
            img2_path=image2,
            model_name="Facenet512",
            detector_backend="opencv"
        )

        print("\nFace Recognition Results")
        print("------------------------")

        if result["verified"]:
            print("Result: Faces Matched")
        else:
            print("Result: Faces Not Matched")

        print("Distance:", round(result["distance"], 4))
        print("Model: FaceNet512")

    except Exception as e:
        print("Error:", e)

    print("\nFace Recognition Completed!")
