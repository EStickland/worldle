

# country = input("Guess county:")

# if country =='France':
#     print('correct!!')
# else:
#     print('wrong!!')

#Import the required Libraries
# from tkinter import *
# from tkinter import ttk
# import random

# #Create an instance of Tkinter frame
# win= Tk()

# #Set the geometry of Tkinter frame
# win.geometry("750x250")

# def display_text():
#    global entry
#    string= entry.get()

# #Initialize a Label to display the User Input
# label=Label(win, text="What is the country?", font=("Courier 22 bold"))
# label.pack()

# # #Create an Entry widget to accept User Input
# # entry= Entry(win, width= 40)
# # entry.focus_set()
# # entry.pack()

# list_countries = ['France','UK','German','Ireland','Italy','Spain']

# country = random.choice(list_countries)

# #Create a Button to validate Entry Widget
# ttk.Button(win, text= "Guess",width= 20, command= display_text).pack(pady=20)

# # while 
# # win.mainloop()
# country_name=''

# def printValue():
#     country_name = entry.get()
#     Label(win, text=f'{country_name}, Registered!', pady=20, bg='#ffbf00').pack()


# entry = Entry(win)
# entry.pack(pady=30)

# # Button(
# #     ws,
# #     text="Register Player", 
# #     padx=10, 
# #     pady=5,
# #     command=printValue
# #     ).pack()

# while country_name != country:
#     printValue()
#     win.mainloop()

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

  
# img = PhotoImage(file="Picture1.png")   
# canvas.create_image(0,0, image=img) 

# def generateImage(country):
#     country_dict = {'UK':'uk.png','Norway':'norway.png','Mexico':'mexico.png'}
#     img = Image.open(f"country_outlines/{country_dict.get(country)}")
#     img = Image.open(f"country_outlines/uk.png")
#     img = img.resize((100,100), Image.ANTIALIAS)
#     pic = ImageTk.PhotoImage(img)
#     return pic

# canvas = Canvas(root, width = 100, height = 100)      
# canvas.pack()    
# canvas.create_image(50,50, image=generateImage(country))

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