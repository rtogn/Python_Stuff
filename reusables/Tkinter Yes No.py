from tkinter import *
from tkinter import messagebox
#import tkMessageBox

var = Tk()
def hello():
   print("Hello World")
def goodbye():
    print("good bye!")
    pass

ans = messagebox.askyesno("Continue?", "Your files have been renamed. \
\nWould you like to continue moving them?")

if ans == 'yes':
    print(ans)
                                     


var.mainloop()
