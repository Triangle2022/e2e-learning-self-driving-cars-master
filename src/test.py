import cv2


name = dataroot + 'IMG/' + imgName.split('\\')[-1]
current_image = cv2.imread(name)