import os
import cv2
import numpy as np

input_dir = "./dataset"
output_dir = "processed_dataset"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(input_dir):

    path = os.path.join(input_dir, file)

    img = cv2.imread(path)

    # remove corrupted images
    if img is None:
        print("Skipping corrupted:", file)
        continue

    # resize
    img = cv2.resize(img, (224, 224))

    # normalize
    img = img / 255.0

    # convert back for saving
    img = (img * 255).astype(np.uint8)

    name = os.path.splitext(file)[0]

    # save original processed image
    cv2.imwrite(os.path.join(output_dir, name + ".jpg"), img)

    # -------- augmentation --------

    # horizontal flip
    flip = cv2.flip(img, 1)
    cv2.imwrite(os.path.join(output_dir, name + "_flip.jpg"), flip)

    # rotate 90 degrees
    rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(output_dir, name + "_rot.jpg"), rotate)

    print("Processed:", file)

print("Dataset preprocessing completed")