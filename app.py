from random import randint
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Number Guessing")

def get_range():
    lowerEntryRange = int(rangeEntryLower.get())
    upperEntryRange = int(rangeEntryUpper.get())
    userEntry = int(userEntryObject.get())
    randNum = randint(lowerEntryRange, upperEntryRange)
    if randNum == userEntry:
        tk.Label(root, text="You got it!").pack()
    else:
        tk.Label(root, text="You got it wrong!").pack()
    

rangeLabel = tk.Label(text="Please enter the range of numbers you will guess from", font="times-medium")
rangeLabel.pack()

rangeEntryLower = tk.Entry(root)
rangeEntryLower.pack()

seperationLabel = tk.Label(text="<------------------------------->", font="times-medium")
seperationLabel.pack()

rangeEntryUpper = tk.Entry(root)
rangeEntryUpper.pack()

userLabel = tk.Label(text="Please enter your guess", font="times-medium").pack()

userEntryObject = tk.Entry(root)
userEntryObject.pack()

button = tk.Button(root, text="Enter", command=get_range)
button.pack()

root.mainloop()