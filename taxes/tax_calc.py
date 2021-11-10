yr = 40000

b1 = 0
b2 = 0
b3 = 0
stddeduct = 12000  #standrad deduction

if yr > stddeduct:
    pass  # since 9525 is less than deduction it is covered within
else:
    total = 0  #100% covered by std deduction

if yr > 38700:  #sets bracket 2 % to pass if >max
    b2 = ((38700-stddeduct) * .12)
elif yr < 38700 and  yr > stddeduct:
    total = ((yr- stddeduct)*.12)+b1



if yr >82500:
    b3=  ((82500-38701) * .22)
    total = b1+b2+b3
elif yr < 82500 and yr > 38700:
        total = ((yr - 38701) *.22)+b1+b2

print(total)
print(yr -total)
