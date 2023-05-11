import cv2

# Open the video file
cap = cv2.VideoCapture("C:/Users/INDHU/Pictures/Camera Roll/WIN_20230502_10_54_26_Pro.mp4")

# Get the number of frames in the video
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Start reading the video from the last frame
frame_idx = total_frames - 1

# Set the video capture object to the last frame
cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)

# Read and display the frames in reverse order
while frame_idx >= 0:
    # Read the frame
    ret, frame = cap.read()

    # Check if the frame is valid
    if ret:
        # Display the frame
        cv2.imshow('Reverse Video', frame)

        # Decrement the frame index
        frame_idx -= 1

        # Set the video capture object to the previous frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)

        # Wait for 25 milliseconds and check if the 'q' key is pressed to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        # If the frame is not valid, break the loop
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
