import numpy as np
import cv2


def split(img):
    color = cv2.imread(img, 1)
    cv2.imshow(img + " Image",color)
    cv2.moveWindow("Image",0,0)
    print(color.shape)
    print(cv2.imread(img))
    height,width,channels = color.shape

    b,g,r = cv2.split(color)

    rgb_split = np.empty([height,width*3,3],'uint8')
    
    rgb_split[:, 0:width] = cv2.merge([b,b,b])
    rgb_split[:, width:width*2] = cv2.merge([g,g,g])
    rgb_split[:, width*2:width*3] = cv2.merge([r,r,r])
    cv2.imwrite(img + "_green.png", cv2.merge([g,g,g]))
    cv2.imshow(img + " Channels",rgb_split)
    cv2.moveWindow("Channels",0,height)

    hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)
    hsv_split = np.concatenate((h,s,v),axis=1)
    cv2.imshow(img + " Split HSV",hsv_split)
    

    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

split("sss.png")


cv2.waitKey(0)
cv2.destroyAllWindows()
