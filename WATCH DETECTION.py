import cv2

# Load the pre-trained model
model = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')

# Load the image
image = cv2.imread("C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-11 104644.png")

# Resize the image to the appropriate size for the model
resized = cv2.resize(image, (300, 300))

# Create a blob from the image
blob = cv2.dnn.blobFromImage(resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)

# Set the input to the model
model.setInput(blob)

# Make predictions on the image
detections = model.forward()

# Loop over the detections
for i in range(0, detections.shape[2]):
    # Extract the confidence and class ID of the current detection
    confidence = detections[0, 0, i, 2]
    class_id = int(detections[0, 0, i, 1])
    
    # Check if the detection is a watch
    if class_id == 81 and confidence > 0.5:
        # Get the bounding box coordinates of the detection
        box = detections[0, 0, i, 3:7] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
        (x1, y1, x2, y2) = box.astype("int")
        
        # Draw the bounding box and label on the image
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f'Watch: {confidence:.2f}'
        cv2.putText(image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# Show the output image
cv2.imshow('Output', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
