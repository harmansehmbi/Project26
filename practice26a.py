# install pytesseract package
import cv2
import pytesseract

image = cv2.imread("data.png", 1)
print(image)  # Numpy Array

print("===========================")

text = pytesseract.image_to_string(image)
print(text)

# Scan an Image : eg. Blood Report Sample.
# Extract Textual Data analyze it with datasets available.
# Perform Supervised Learning with Regression.



