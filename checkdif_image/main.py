from deepface import DeepFace
import sys

img1 = sys.argv[1]
img2 = sys.argv[2]

result = DeepFace.verify(img1, img2)

print("Verified: ", result)