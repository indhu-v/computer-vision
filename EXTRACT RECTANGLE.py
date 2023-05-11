import cv2

# Load the image
image = cv2.imread("C:/Users/INDHU/Pictures/Screenshots/Screenshot 2023-05-11 104644.png")

# Draw a rectangle
x, y, w, h = 100, 100, 200, 300
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Extract the object inside the rectangle
object_roi = image[y:y+h, x:x+w]

# Display the image with the rectangle and the extracted object
cv2.imshow("Image with rectangle and object", image)
cv2.imshow("Extracted object", object_roi)
cv2.waitKey(0)
cv2.destroyAllWindows()
