import numpy as np
import cv2, pyautogui

im = pyautogui.screenshot(region=(0,0, 300, 400))
ims = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
cv2.imshow("Basic Binary",ims)
def moves(img):
    img = cv2.imread(img, 1)
    height = img.shape[0]
    width = img.shape[1]
    total = 0
    count = 0
    for row in range(0, len(img),15):
        for col in range(0, width, 25):
            total += img[row][col][1]
            count += 1
    avrg = total / (count)
    print(f"count: {count}")
    return (avrg)
           

print( moves('splash.png') )
print( moves('bobS.png') )
