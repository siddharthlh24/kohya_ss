import cv2
import os

# Set input and output folders
input_folder = "crop_input_folder/"
output_folder = "crop_output_folder/"   

# Set the desired output resolution (in pixels)
output_resolution = 512

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
if not os.path.exists(input_folder):
    os.makedirs(input_folder)
    
# Loop through all images in the input folder
for filename in os.listdir(input_folder):
    try:
        # Load the image
        img = cv2.imread(os.path.join(input_folder, filename), cv2.IMREAD_ANYCOLOR)

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Loop through all detected faces
        for (x, y, w, h) in faces:
            # Extract the face from the image
            face = img[y:y+h, x:x+w]

            # Resize the face to the desired output resolution
            resized_face = cv2.resize(face, (output_resolution, output_resolution))

            # Save the resized face to the output folder
            output_filename = os.path.splitext(filename)[0] + "_face_" + str(x) + "_" + str(y) + ".jpg"
            cv2.imwrite(os.path.join(output_folder, output_filename), resized_face)
    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

# Print a message when the process is completed
print("Process completed")
