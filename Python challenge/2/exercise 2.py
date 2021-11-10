text = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

it = 0
textelement = text[it]
solution = ''


for it in range(len(text)):
    truval = list.index(textelement)
    cipherval = truval+2
    textelement = text[it]
    it = it+1
    if it >= (len(text)):
        print(solution)
        break
        
    if text[it] not in list:
        solution= solution + f'{text[it]}'
        
        
    else:
        solution= solution + f'{list[cipherval]}'
        
       
    
    
   




           
        

            
   
      
    

       
