
import wikipedia

import tkinter as tk
root = tk.Tk()


canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

offline= False
# def getSquareRoot():
#     x1 = entry1.get()
#
#     label1 = tk.Label(root, text=float(x1) ** 0.5)
#     canvas1.create_window(200, 230, window=label1)
def randomFlag(offline=True):
    ls_countries = ['Afghanistan','Albania','Algeria','American Samoa','Andorra','Angola',
                    'Anguilla', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia',
                    'Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus',
                    'Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia and Herzegovina',
                    'Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia',
                    'Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile',
                    'China','Colombia','Comoros','Democratic Republic of the Congo','Congo, Republic of',
                    'Costa Rica',"Côte D'ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark',
                    'Djibouti','Dominica','Dominican Republic','East Timor','Ecuador','Egypt','El Salvador',
                    'Equatorial Guinea','Eritrea','Estonia','Ethiopia','Faroe Islands','Fiji','Finland',
                    'France','French Guiana','French Polynesia','Gabon','The Gambia','Georgia','Germany',
                    'Ghana','Greece','Greenland','Grenada','Guadeloupe','Guam','Guatemala','Guinea',
                    'Guinea-Bissau','Guyana','Haiti','Honduras','Hong Kong','Hungary']
    if not offline:
        wikipage = wikipedia.page('Flag of Benin')
        print(wikipage.images[0])

# def guessFlag():
#
# button1 = tk.Button(text='Guess the flag', commaxnd=getSquareRoot)
# canvas1.create_window(200, 180, window=button1)
#
# root.mainloop()