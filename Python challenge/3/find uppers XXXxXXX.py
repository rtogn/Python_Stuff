text = "sdasdsadasdaAAAxAAA"

#text[0].islower() 
#if text[0].islower() == True:
 #   print("its true")

num = 0
if text[num].isupper() == True and text[num+1].isupper() == True and text[num+2].isupper() == True \
   and text[num+3].islower() == True and text[num+4].isupper() == True and text[num+5].isupper() == True and text[num+6].isupper() == True:
    print(text[num]+text[num+1]+text[num+2]+text[num+3]+text[num+4]+text[num+5]+text[num+6])
else:
    num += 1
    continue
