import os
date = input ("what is today's Month and Year?  ")
number = 1
filename = str(number) + date


print (f'Ok, today is {date}, creating files on Desktop!')

while number <= 31:
   
    os.chdir ('C:/Users/Lobster/Desktop/Pythontest')
    os.makedirs(f'{date}/{filename}/Eligibility')
    os.chdir (f'C:/Users/Lobster/Desktop/Pythontest/{date}/{filename}')
    os.mkdir('Single Reqs')
    os.mkdir('Clin Packets')
    number = number + 1
    filename = str(number) + date
