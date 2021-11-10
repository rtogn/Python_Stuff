import os
print('Hello, welcome to the 31 day file creator version 1.0! February can suck it! -Made by Rob Tognoni')
print('')
date = input ("What is the Month and Year? (MonthYYYY): ")
number = 1
filename = str(number) + date
user = os.getlogin()

print('')
print (f'Ok, today is {date}, creating 31 batched files on the Desktop!')
print('')
print(f'By the way, {user}, if the file already exists an error will display! Rob was too lazy to code in real error checking.')

while number <= 31:
   
    os.chdir (f'C:/Users/{user}/Desktop')
    os.makedirs(f'{date}/{filename}/Eligibility')
    os.chdir (f'C:/Users/{user}/Desktop/{date}/{filename}')
    os.mkdir('Single Requisitions')
    os.mkdir('Packets')
    os.chdir (f'C:/Users/{user}/Desktop/{date}/{filename}/Eligibility')
    os.mkdir('Declined')
    os.mkdir('Approved')
    os.mkdir('Clinician')
    os.mkdir('Patient Pay')
    os.mkdir('Resolved - Accounting to Bill')
    os.mkdir('Clinic')
    number = number + 1
    filename = str(number) + date
