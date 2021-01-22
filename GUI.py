import tkinter as tk
import requests
from tkinter import font
from tkinter import PhotoImage
HEIGHT = 500
WIDTH = 500

def formatres(weather):
       try:
           name = (weather['name'])
           weatherdes= (weather['weather'][0]['description'])
           temp = (weather['main']['temp'])

           label['text'] = (str(name) + ' \n' + str(weatherdes)+ " \n" + str(temp) + '(°C)')
       except:
           label['text'] = 'Error'

def get_weather(city):
   weather_key = '03e3c1ec16cc2519071632ca95d12344'
   url = 'http://api.openweathermap.org/data/2.5/weather'
   params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
   response = requests.get(url, params=params)
   weather = response.json()
   label['text'] = formatres(weather)



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()

background_image = PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg= '#80c1ff', bd = 5 )
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor = 'n')

entry = tk.Entry(frame, font = 40)
entry.place (relwidth=0.65, relheight=1)

button = tk.Button(frame, text= "Get Weather", font =('Courier', 11), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight =1, relwidth=0.3)

lf = tk.Frame(root, bg = '#80c1ff' , bd = 10)
lf.place(relx=0.5, rely =0.25, relwidth=0.75, relheight=0.6, anchor= 'n')

label = tk.Label(lf, font=('Courier', 25))
label.place(relwidth=1, relheight=1)

root.mainloop()


