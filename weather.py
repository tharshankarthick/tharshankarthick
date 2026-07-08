import requests
from tkinter import *
from PIL import Image, ImageTk

API_key="ADD YOUR API KEY"

win=Tk()

win.geometry('720x360')

lab=Label(win,text='Enter City to check weather:',font=('Courier New',14,'bold'))
lab.grid(row=0,column=0)

entry=Entry(win,font=('Comic Sans',16,'bold'),width=30)
entry.grid(row=0,column=1)

def add():
    listbox.delete(0,'end')
    city_name=entry.get()
    
    url=f"""https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}"""
    
    response=requests.get(url)
    
    data=response.json()
    
    if response.status_code==200:
        listbox.insert(END,f"""City: {data["name"]}""")
        listbox.insert(END,f"""temperature: {data["main"]["temp"]-273.15:.2f}°C""")
        listbox.insert(END,f"""Humidity: {data["main"]["humidity"]}%""")
        listbox.insert(END,f"""Weather: {data["weather"][0]["description"]}""")
        listbox.insert(END,f"""Wind Speed: {data["wind"]["speed"]}m/s""")
        listbox.config(height=listbox.size())
        
    else:
        listbox.insert(END,"City Not Found")

    if ((data["main"]["temp"])-273.15)<0 :
        img=Image.open("freeze.png")
        reimg=img.resize((300,200))
        pic=ImageTk.PhotoImage(reimg)
        label=Label(image=pic)
        label.image=pic
        label.grid(row=3,column=1)
        lab=Label(win,text='Freeze Weather',font=('Courier New',14,'bold'))
        lab.grid(row=4,column=1)

    elif (((data["main"]["temp"])-273.15)>0) and (((data["main"]["temp"])-273.15)<10) :
        img=Image.open("chill.png")
        reimg=img.resize((300,200))
        pic=ImageTk.PhotoImage(reimg)
        label=Label(image=pic)
        label.image=pic
        label.grid(row=3,column=1)
        lab=Label(win,text='Chill Weather',font=('Courier New',14,'bold'))
        lab.grid(row=4,column=1)

    elif (((data["main"]["temp"])-273.15)>10) and (((data["main"]["temp"])-273.15)<20) :
        img=Image.open("rain.png")
        reimg=img.resize((300,200))
        pic=ImageTk.PhotoImage(reimg)
        label=Label(image=pic)
        label.image=pic
        label.grid(row=3,column=1)
        lab=Label(win,text='Rainy Weather',font=('Courier New',14,'bold'))
        lab.grid(row=4,column=1)

    elif (((data["main"]["temp"])-273.15)>20) and (((data["main"]["temp"])-273.15)<30) :
        img=Image.open("mild.png")
        reimg=img.resize((300,200))
        pic=ImageTk.PhotoImage(reimg)
        label=Label(image=pic)
        label.image=pic
        label.grid(row=3,column=1)
        lab=Label(win,text='Mild Weather',font=('Courier New',18,'bold'))
        lab.grid(row=4,column=1)

    elif (((data["main"]["temp"])-273.15)>30) and (((data["main"]["temp"])-273.15)<40) :
        img=Image.open("warm.jpg")
        reimg=img.resize((300,200))
        pic=ImageTk.PhotoImage(reimg)
        label=Label(image=pic)
        label.image=pic
        label.grid(row=3,column=1)
        lab=Label(win,text='Hot Weather',font=('Courier New',18,'bold'))
        lab.grid(row=4,column=1)

    elif ((data["main"]["temp"])-273.15)>40 :
        img=Image.open("hot.png")
        reimg=img.resize((300,200))
        pic=ImageTk.PhotoImage(reimg)
        label=Label(image=pic)
        label.image=pic
        label.grid(row=3,column=1)
        lab=Label(win,text='Very Hot!!!!',font=('Courier New',18,'bold'))
        lab.grid(row=4,column=1)

button=Button(win,text='Click me to submit city selection',font=('Comic Sans',14,'bold'),command=add)
button.grid(row=1,column=1)

listbox=Listbox(win,font=('Courier New',16,'bold'),width=25)
listbox.grid(row=3,column=0)

win.mainloop()
