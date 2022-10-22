
############################ SETUP ################################
##### READ IN PACKAGES #####
from os import lstat
import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from math import radians, cos, sin, asin, sqrt
import pandas as pd

##### CREATE ROOT #####
root = Tk()
root.geometry("300x500")

####################################################################

######################## DATA/PARAMETERS #############################
list_countries = ['Afghanistan',
 'Angola',
 'Albania',
 'United Arab Emirates',
 'Argentina',
 'Armenia',
 'Antarctica',
 'French Southern and Antarctic Lands',
 'Australia',
 'Austria',
 'Azerbaijan',
 'Burundi',
 'Belgium',
 'Benin',
 'Burkina Faso',
 'Bangladesh',
 'Bulgaria',
 'The Bahamas',
 'Bosnia and Herzegovina',
 'Belarus',
 'Belize',
 'Bolivia',
 'Brazil',
 'Brunei',
 'Bhutan',
 'Botswana',
 'Central African Republic',
 'Canada',
 'Switzerland',
 'Chile',
 'China',
 'Ivory Coast',
 'Cameroon',
 'Democratic Republic of the Congo',
 'Republic of the Congo',
 'Colombia',
 'Costa Rica',
 'Cuba',
 'Northern Cyprus',
 'Cyprus',
 'Czech Republic',
 'Germany',
 'Djibouti',
 'Denmark',
 'Dominican Republic',
 'Algeria',
 'Ecuador',
 'Egypt',
 'Eritrea',
 'Spain',
 'Estonia',
 'Ethiopia',
 'Finland',
 'Fiji',
 'Falkland Islands',
 'France',
 'Gabon',
 'United Kingdom',
 'Georgia',
 'Ghana',
 'Guinea',
 'Gambia',
 'Guinea Bissau',
 'Equatorial Guinea',
 'Greece',
 'Greenland',
 'Guatemala',
 'Guyana',
 'Honduras',
 'Croatia',
 'Haiti',
 'Hungary',
 'Indonesia',
 'India',
 'Ireland',
 'Iran',
 'Iraq',
 'Iceland',
 'Israel',
 'Italy',
 'Jamaica',
 'Jordan',
 'Japan',
 'Kazakhstan',
 'Kenya',
 'Kyrgyzstan',
 'Cambodia',
 'South Korea',
 'Kosovo',
 'Kuwait',
 'Laos',
 'Lebanon',
 'Liberia',
 'Libya',
 'Sri Lanka',
 'Lesotho',
 'Lithuania',
 'Luxembourg',
 'Latvia',
 'Morocco',
 'Moldova',
 'Madagascar',
 'Mexico',
 'Macedonia',
 'Mali',
 'Myanmar',
 'Montenegro',
 'Mongolia',
 'Mozambique',
 'Mauritania',
 'Malawi',
 'Malaysia',
 'Namibia',
 'New Caledonia',
 'Niger',
 'Nigeria',
 'Nicaragua',
 'Netherlands',
 'Norway',
 'Nepal',
 'New Zealand',
 'Oman',
 'Pakistan',
 'Panama',
 'Peru',
 'Philippines',
 'Papua New Guinea',
 'Poland',
 'Puerto Rico',
 'North Korea',
 'Portugal',
 'Paraguay',
 'Qatar',
 'Romania',
 'Russia',
 'Rwanda',
 'Western Sahara',
 'Saudi Arabia',
 'Sudan',
 'South Sudan',
 'Senegal',
 'Solomon Islands',
 'Sierra Leone',
 'El Salvador',
 'Somaliland',
 'Somalia',
 'Republic of Serbia',
 'Suriname',
 'Slovakia',
 'Slovenia',
 'Sweden',
 'Swaziland',
 'Syria',
 'Chad',
 'Togo',
 'Thailand',
 'Tajikistan',
 'Turkmenistan',
 'East Timor',
 'Trinidad and Tobago',
 'Tunisia',
 'Turkey',
 'Taiwan',
 'United Republic of Tanzania',
 'Uganda',
 'Ukraine',
 'Uruguay',
 'United States of America',
 'Uzbekistan',
 'Venezuela',
 'Vietnam',
 'Vanuatu',
 'West Bank',
 'Yemen',
 'South Africa',
 'Zambia',
 'Zimbabwe']

df_lat_long = pd.read_csv('countries/country_lat_long.csv')
list_countries = [x for x in list_countries if x in df_lat_long['country'].tolist()]

global current_score
current_score = 0

global guess_count
guess_count = 0

global max_rounds
max_rounds = 3

global round_count
round_count = 1
######################## FUNCTIONS #############################
def imageGenerator(country):
    global pic
    img = Image.open(f"countries/{country}.png")
    img = img.resize((100,100), Image.ANTIALIAS)
    pic = ImageTk.PhotoImage(img)
    global canvas
    canvas = Canvas(root, width = 100, height = 100)      
    canvas.pack()   
    canvas.create_image(50,50, image=pic)

def search(event):
    value = event.widget.get()
    if value == '':
        combo_box['value'] = list_countries
    else:
        data = []
        for item in list_countries:
            if value.lower() in item.lower():
                data.append(item)
        combo_box['value'] = data

def isCorrect(x):
    global current_score
    if x == country:
        current_score +=(5-(guess_count-1))
        scoreUpdate(current_score)
        return('Correct')
    else:
        if guess_count==5:
            return('Failed')
        else:
            return('Try Again')

def myClick():
    global guess_count
    global round_count
    guess_count +=1
    lat1, long1 = getLatLong(country)
    lat2, long2 = getLatLong(combo_box.get())
    distance = calculateDistance(lat1, lat2, long1, long2)
    direction = calculateDirection(lat1, lat2, long1, long2)
    result = isCorrect(combo_box.get())
    myLabel2 = Label(root, text=result)
    myLabel2.pack()
    myLabel3 = Label(root, text=f'{guess_count} {combo_box.get()}: {round(distance)} kms {direction}')
    myLabel3.pack()
    if (result == 'Correct') | (guess_count==5):
        if round_count == max_rounds:
            finish()
        else: 
            round_count +=1
            Button(root,text="New Game", command=clear_frame).pack()

def clear(widgets_to_clear):
    for widget in widgets_to_clear:
        widget.destroy()

def exit_button():
    exit_button = Button(root, text="Exit", command=root.destroy)
    exit_button.pack(pady=20)

def makeGuess():
    myButton = Button(root,text="Guess", command=myClick)
    myButton.pack()

def appTitle():
    myLabel = Label(root, text="Guess the country")
    myLabel.pack()

def countryBox():
    global combo_box
    combo_box = ttk.Combobox(root, value=list_countries)
    combo_box.bind('KeyRelease',search)
    combo_box.pack()

def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()
    allFuncs()

def score():
    global myLabel
    myLabel = Label(root, text=f"Score: {current_score}")
    myLabel.pack()

def roundLabel():
    # global roundLabel
    roundLabel = Label(root, text=f"Round: {round_count}")
    roundLabel.pack()

def scoreUpdate(current_score):
    myLabel.config(text=f"Score: {current_score}")


def calculateDistance(lat1, lat2, lon1, lon2):
     
    # The math module contains a function named
    # radians which converts from degrees to radians.
    lon1 = radians(lon1)
    lon2 = radians(lon2)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
      
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
 
    c = 2 * asin(sqrt(a))
    
    # Radius of earth in kilometers. Use 3956 for miles
    r = 6371
      
    # calculate the result
    return(c * r)

def getLatLong(country):
    lat = df_lat_long[df_lat_long['country']==country].values[0][1]
    long = df_lat_long[df_lat_long['country']==country].values[0][2]
    return lat, long


def calculateDirection(lat_a,lat_b, long_a,  long_b):
    north = '\U00002B06'
    north_west = '\U00002196'
    north_east = '\U00002197'
    south = '\U00002B07'
    south_west = '\U00002199'
    south_east = '\U00002198'
    east = '\U000027A1'
    west = '\U00002B05'
    if abs(long_a-long_b) > abs(lat_a-lat_b):
        if long_a > long_b:
            direction = '\u2B05'
            direction = 'East'+east
        else:
            direction = '\u27A1'
            direction = 'West'+west
    else:
        if lat_a > lat_b:
            direction = '\u2B06'
            direction = 'North'+north
        elif lat_a < lat_b:
            direction = '\u2B07'
            direction = 'South'+south
        else:
            direction=''
    return direction

def cheatButton():
    cheatButton = Button(root,text="Cheat", command=showAnswer)
    cheatButton.pack()

def showAnswer():
    answer = Label(root, text=f'ANSWER: {country}')
    answer.pack()


def guessCountReset():
    global guess_count
    guess_count=0

def roundCountReset():
    global round_count
    round_count=0


def finish():
    appTitle()
    for widgets in root.winfo_children():
        widgets.destroy()
    final_score = Label(root, text=f'GAME OVER\nFINAL SCORE\n {current_score}/{max_rounds*5}')
    final_score.pack()
    exit_button()




def welcomeScreen():
    gameTitle = Label(root, text=f'WELCOME TO WORLDLE \U0001F30D ')
    gameTitle.pack()
    roundRequestLabel = Label(root, text=f'How many rounds would you like?')
    roundRequestLabel.pack()
    global roundRequest
    roundRequest = Entry(root)
    roundRequest.pack()
    game_combo_box = ttk.Combobox(root, value=['Country Outlines'])
    game_combo_box.pack()
  
    startGame = Button(root,text="Start Game", command=updateRoundNumber)
    startGame.pack()

def updateRoundNumber():
    global max_rounds
    max_rounds = int(roundRequest.get())
    clear_frame()

######################## STATIC CONTENT #############################


def allFuncs():
    
    print('max_rounds', max_rounds)
    global country
    country = random.choice(list_countries)
    roundLabel()
    guessCountReset()
    appTitle()
    score()
    imageGenerator(country)
    countryBox()
    makeGuess()
    cheatButton()
    exit_button()


welcomeScreen()

root.mainloop()
