from string import maketrans

intab = 'abcdefghijklmnopqrstuvwxyz'
outtab = 'cdefghijklmnopqrstuvwxyzab'
trantab = maketrans(intab, outtab)

str = "http://www.pythonchallenge.com/pc/def/map.html"
print (str.translate(trantab))
