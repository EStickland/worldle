# country = input("Guess county:")

import random
from tkinter import *
from PIL import Image, ImageTk
root = Tk()
myLabel = Label(root, text="Guess the country")
myLabel.pack()


list_countries = ['Norway','UK','Mexico']

country = random.choice(list_countries)

def isCorrect(x):
    if x == country:
        return('Correct')
    else:
        return('Try Again')

def myClick():
    myLabel2 = Label(root, text=isCorrect(e.get()))
    myLabel2.pack()

canvas = Canvas(root, width = 100, height = 100)      
canvas.pack()
country_dict = {'UK':'uk.png','Norway':'norway.png','Mexico':'mexico.png'}
img = Image.open(f"country_outlines/{country_dict.get(country)}")
# img = Image.open(f"country_outlines/uk.png")
img = img.resize((100,100), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(img)
canvas = Canvas(root, width = 100, height = 100)      
canvas.pack()    
canvas.create_image(50,50, image=pic)

def clear(*widgets):
    for widget in widgets:
        widget.destroy()


e = Entry(root, )
e.pack()
e.insert(0, "Country")

myButton = Button(root,text="Guess", command=myClick).pack()

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)

root.mainloop()
