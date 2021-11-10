import numpy as np
import pyautogui as auto
import cv2, time, random


auto.keyDown('alt')
auto.press('tab')
auto.keyUp('alt')





def pixCheck(top, floor, lowest, count, step):

    for yCord in range( 0, verticalRangeHalf, step):
        for xCord in range (horizontalRangeLeft, horizontalRangeRight, step):
            count +=1
            if img[yCord][xCord][1] <= 40:
                lowest = img[yCord][xCord][1]
                return  ( [yCord, xCord, lowest, count] )
 
def average(img):

    height = img.shape[0]
    width = img.shape[1]
    total = 0
    count = 0    
    for row in range(0, len(img)):
        for col in range(0, width): 
            total += img[row][col][1]
            count += 1
    avrg = total / (count)
    #print(f"count: {count}")
    return (avrg)


image = auto.screenshot()
img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

lowest = 255
#auto.press('5')
horizontalRangeLeft = int(img.shape[1]*(1/3))
horizontalRangeRight = int(img.shape[1]*(2/3))
verticalRangeHalf = int(len(img)/2)
step = int(0.000006*(len(img) * img.shape[1]))



run = pixCheck(0, len(img), lowest, 0, step)
y = run[0]
x = run[1]
print(f"moving to pix {x}, {y}")
auto.moveTo(x, y, duration = .2)

#Screenshot slightly above bobber 70x70 to check. Then calc average value of color channel green across the image
ims = cv2.cvtColor(np.array(auto.screenshot(region=((x-20),(y-20), 70, 70))), cv2.COLOR_RGB2BGR)
baseAverage = average(ims)
checkAverage = baseAverage
#q = cv2.imwrite("BobTest.png",ims)

while ( (baseAverage / checkAverage ) > .92 ):
	checkImg = cv2.cvtColor(np.array(auto.screenshot(region=((x-20),(y-20), 70, 70))), cv2.COLOR_RGB2BGR)
	checkAverage = average(checkImg)
	#print(f"base: {baseAverage}, check: {checkAverage}, percent: {baseAverage / checkAverage}") 
	time.sleep(0.3)
#print("broke loop!")    
auto.click(button='right')
time.sleep(2)
#print("casting rod!")
auto.press('5')
#time.sleep(2)

#x = input("Any key to exit")


