import cv2

# Correct path to the Haar cascade file
face_cascade = cv2.CascadeClassifier(r'd:\myapp\face_ai\haarcascade_frontalface_default.xml')

# Correct path to the image file
img = cv2.imread(r'd:\myapp\face_ai\your_image.jpg')

# Check if the image was loaded correctly
if img is None:
    print("Error: Could not read the image file.")
    exit(1)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the result
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
