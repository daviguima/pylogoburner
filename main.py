import cv2
import numpy as np


logo = cv2.imread("imgs/marca_dagua.png")
nice_house = cv2.imread("/imgs/nice-house.png")

h_img, w_img, _ = nice_house.shape

scale_percent = 60 # percent of original size
width = int(logo.shape[1] * scale_percent / 100)
height = int(logo.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
logo = cv2.resize(logo, dim, interpolation = cv2.INTER_AREA)


h_logo, w_logo, _ = logo.shape
logo.shape,nice_house.shape


center_y = int(h_img / 2)
center_x = int(w_img / 2)
center_y,center_x


top_y = center_y - int(h_logo / 2)
bottom_y = top_y + h_logo
left_x = center_x - int(w_logo / 2)
right_x = left_x + w_logo

(top_y,bottom_y,left_x,right_x)


# Get ROI
roi = nice_house[top_y:bottom_y, left_x:right_x]
# nice_house[top_y:bottom_y, left_x:right_x] = logo


result = cv2.addWeighted(roi, 1, logo, 0.2, 0)


nice_house[top_y:bottom_y, left_x:right_x] = result

# Save the modified image
cv2.imwrite("/imgs/my_first_image.jpg", nice_house)