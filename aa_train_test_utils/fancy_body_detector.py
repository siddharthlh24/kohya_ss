import os
import cv2

# Define the input folder containing the images
input_folder = 'crop_input_folder'

# Create an output folder to save the cropped images
output_folder = 'crop_output_folder'
os.makedirs(output_folder, exist_ok=True)

# Load the pre-trained YOLOv3 model
weights_path = 'yolov3.weights'
config_path = 'yolov3.cfg'
net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

# Load the class labels
labels_path = 'coco.names.txt'
with open(labels_path, 'r') as f:
    labels = f.read().splitlines()

# Specify the target backend and target computation device (GPU if available)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)  # Change to cv2.dnn.DNN_TARGET_CUDA if GPU is available

# Process each image in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)

        # Create a blob from the image and set it as the input to the network
        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)

        # Perform forward pass and get the output layer names
        layer_names = net.getLayerNames()
        output_layers = net.getUnconnectedOutLayersNames()
        detections = net.forward(output_layers)

        # Iterate over the detected objects and filter for person detections
        for detection in detections:
            for obj in detection:
                scores = obj[5:]
                class_id = scores.argmax()
                confidence = scores[class_id]

                if class_id == 0 and confidence > 0.5:  #
                    # Extract bounding box coordinates
                    center_x, center_y, width, height = obj[0:4] * [image.shape[1], image.shape[0], image.shape[1], image.shape[0]]
                    x, y = int(center_x - width / 2), int(center_y - height / 2)
                    x_max, y_max = x + int(width), y + int(height)

                    # Crop the image to the region of the detected person
                    cropped_image = image[y:y_max, x:x_max]

                    # Save the cropped image
                    output_path = os.path.join(output_folder, filename)
                    cv2.imwrite(output_path, cropped_image)
                    print(f"Cropped image saved: {output_path}")