import os

user = os.getlogin()

x = os.listdir(f"C:/Users/{user}/Desktop/Python Projects")

for i in x:
    print(i)
