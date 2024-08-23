## test picture

import numpy as np
import cv2
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import pickle
import sys

size=224

model="mod/model"
labelbin="mod/lablebin"
path=sys.argv[1]


image = cv2.imread(path)
# output = image.copy()

# pre-process the image for classification
image = cv2.resize(image, (size, size))
image = image.astype("float") / 127.5-1
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# load the trained convolutional neural network and the label
# binarizer
print("[INFO] loading network...")
model = load_model(model)
lb = pickle.loads(open(labelbin, "rb").read())
# classify the input image
print("[INFO] classifying image...")
proba = model.predict(image)[0]
idx = np.argmax(proba)
label = lb.classes_[idx]

if (label=="greeneye" and proba[idx]<0.5):
	label="else"
elif (proba[idx]<0.9):
	label="else"

birds = {
"whitehead" : "白頭翁",
"pica" : "喜鵲",
"yen" : "燕子",
"sparrow" : "麻雀",
"night" : "夜鷺",
"greeneye" : "綠繡眼",
"else":"看起來是其他東西喔"}
print(birds[label])
if(label!="else"):
	print(round(proba[idx]*100,2))
'''
filename = os.path.basename(path)
correct = "correct" if filename.rfind(label) != -1 else "incorrect"
# build the label and draw the label on the image
label = "{}: {:.2f}% ({})".format(label, proba[idx] * 100, correct)
output = imutils.resize(output, width=400)
cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
	0.7, (0, 255, 0), 2)
# show the output image
print("[INFO] {}".format(label))
cv2_imshow(output)
cv2.waitKey(0)
'''
