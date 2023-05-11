import cv2

# Load the YOLO object detection model
net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')

# Set the names of the classes to detect
classes = []
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Set the minimum confidence level for object detection
conf_threshold = 0.5

# Open the video capture object to read from the video file
cap = cv2.VideoCapture('video.mp4')

# Set the output video codec and dimensions
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))

# Read the frames from the video and detect objects in real-time
while True:
    # Read the frame
    ret, frame = cap.read()

    # Create a blob from the input frame
    blob = cv2.dnn.blobFromImage(frame, 1/255, (416, 416), swapRB=True, crop=False)

    # Set the input of the YOLO network to the blob
    net.setInput(blob)

    # Get the output of the YOLO network
    output_layers = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers)

    # Parse the output of the YOLO network and draw bounding boxes around the detected vehicles
    class_ids = []
    confidences = []
    boxes = []
    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > conf_threshold and class_id == 2:
                center_x = int(detection[0] * frame.shape[1])
                center_y = int(detection[1] * frame.shape[0])
                w = int(detection[2] * frame.shape[1])
                h = int(detection[3] * frame.shape[0])
                x = int(center_x - w/2)
                y = int(center_y - h/2)
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, 0.4)

    for i in indices:
        i = i[0]
        box = boxes[i]
        x, y, w, h = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Write the resulting frame to the output video file
    out.write(frame)

    # Display the resulting frame
    cv2.imshow('Vehicle Detection', frame)

    # Wait for 1 millisecond and check if the 'q' key is pressed to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object, output video object, and destroy all windows
cap.release()
out.release()
cv2.destroyAllWindows()
