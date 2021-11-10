import numpy as np
import pyautogui as auto
import cv2, time


auto.keyDown('alt')
#time.sleep(0.1)
auto.press('tab')
#auto.press('tab')
#time.sleep(0.1)
auto.keyUp('alt')

image = auto.screenshot()
img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)#
#ret, img = cv2.threshold(img,55,255,cv2.THRESH_BINARY)
#cv2.imshow("Basic Binary",img)

#cv2.imwrite("in_memory_to_disk.png", img)

#img = cv2.imread("menethilB.jpg", 1)
#img = cv2.imread("10x4_test1.png", 1)
rowSave = 0
colSave = 0
lowest = 255

horizontalRangeLeft = int(img.shape[1]*(1/3))
horizontalRangeRight = int(img.shape[1]*(2/3))
verticalRangeHalf = int(len(img)/2)
step = int(0.000006*(len(img) * img.shape[1]))

def pixCheck(top, floor, lowest, count, step):

    for row in range( 0, verticalRangeHalf, step):
        for col in range (horizontalRangeLeft, horizontalRangeRight, step):
            count +=1
            if img[row][col][1] <= 40:
                lowest = img[row][col][1]
                return  ( [row, col, lowest, count] )
 
       
run = pixCheck(0, len(img), lowest, 0, step)

'''
if run[2] > 40:
	run = pixCheck(verticalRangeHalf, len(img), lowest, run[3])
	'''

          
  
print(run[3])
#print(run)

#auto.moveTo(colSave, rowSave, duration = 0)
auto.moveTo(run[1], run[0], duration = 0)
auto.click(button='right')
time.sleep(0.5)
auto.press('5')
#x = input("Any key to exit")

'''
if img[row][col][1] < lowest:

lowest = img[row][col][1]
#print(img[row][col][1])
'''

