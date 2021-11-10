def tax (yr):
    b1 = 0
    b2 = 0 #init bracket placeholders, gets muddled without these
    b3 = 0
    stddeduct = 12000  # set to variable to addon later for other filing types

    if yr > stddeduct:
        pass  # since 9525 is less than deduction it is covered within. later add toggle for deduction on/off this was just easier
    else:
        total = 0  # effectively 100% covered by std deduction

    if yr > 38700:  # sets bracket 2 % to pass if >max
        b2 = ((38700 - stddeduct) * .12)
    elif yr < 38700 and yr > stddeduct:
        total = ((yr - stddeduct) * .12) + b1

    if yr > 82500:
        b3 = ((82500 - 38701) * .22)
        total = b1 + b2 + b3
    elif yr < 82500 and yr > 38700:
        total = ((yr - 38701) * .22) + b1 + b2

    ftax = "%.2f" % total
    takehome = "%.2f" % (yr -total)
    monthfed = "%.2f" % ((yr-total) / 12)
    fedsocsec = "%.2f" % ((yr*0.9235)-total)  #6.2% social sec 1.45% medicare 100% jewry
    fedsocmon = "%.2f" % (((yr*0.9235)-total)/12)
    fedsocbimon = "%.2f" % ((((yr * 0.9235) - total) / 12)/2)  #this is a clusterfuck because it wont take these vars as ints...

    print("\n*************************************")

    print(f"**Based on the 2018 Standard Deduction of ${stddeduct} at tax time")

    print(f"Total federal tax: ${ftax}")

    print(f"\nAdjusted monthly pay (includes tax return): ${monthfed}\nAfter Social Security "
          f"& Medicare: ${fedsocmon}\n\nBi-monthly: ${fedsocbimon}")

    print(f"\nTotal takehome after federal tax: ${takehome} \nAfter Social Security & Medicare: ${fedsocsec}")

    print("*************************************")

def sal (pay, worked, deduction):
    week = pay * worked
    pw = "%.2f" % week  #makes week 2 digit float


    print("*************************************")
    print(f"Per week pay: ${pw}")

    month = week * 4.35 -deduction
    pm = "%.2f" % month #makes month 2 digit float
    print (f"\nAverage monthly pay: ${pm}")

    bimonth = month/2
    pbi = "%.2f" % bimonth #makes bimonth 2 digit float
    print(f"\nBi-monthly: ${pbi}")

    year = week * 52
    py = "%.2f" % year #makes year 2 digit float, really not sure why it wont let me do year = "%.2f" % (week *52)
    print(f"\nTotal per year: ${py}")
    tax(year)



p = float(input("what is the pay per hour? " ))

w = float(input ("How many hours worked per week? "))
deds = float(input("Other monthly deductions or bills (Enter 0 if none): " ))
print(f"\nUSER INPUT: ${p} per hour and {w} hours per week\nThis software will only provide a close estimate of pay\
 and does not include things like state taxes")
sal (p, w, deds)
input("Press Enter to exit")




