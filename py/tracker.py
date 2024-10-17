import tkinter
import tkintermapview
import ttkbootstrap as ttk
import phonenumbers
import tkinter.font as tkFont

from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox
from ttkbootstrap.constants import *

from opencage.geocoder import OpenCageGeocode
#pylint: skip-file

app = ttk.Window(themename = 'solar')
app.geometry("700x700")
app.title("Phone Tracker")
app.resizable(width=False, height=False)

#Functions
def get_result():
    num = number.get(1.0, END)
    try:
        num1 = phonenumbers.parse(num)
    except:
        messagebox.showerror("Error", "Enter a 10 digit number with proper country code")

    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")

    key = '5fe8f95c5a844626b44e8c89aedc3f10'

    ocg = OpenCageGeocode(key)
    query = str(location)
    results = ocg.geocode(query)

    lat = results[0]["geometry"]["lat"]
    lng = results[0]["geometry"]["lng"]

    my_lab = LabelFrame(app)
    my_lab.pack(pady=20)

    map_widget = tkintermapview.TkinterMapView(my_lab, width=650, height=480, corner_radius=4)
    map_widget.set_position(lat, lng)
    map_widget.set_marker(lat, lng)
    map_widget.set_zoom(11)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.pack()

    adrs = tkintermapview.convert_coordinates_to_address(lat, lng)

    result.insert(END, "Latitude is :  " + str(lat))
    result.insert(END, "\nLongitude is :  " + str(lng))
   
    result.insert(END, "\nThe SIM card of this number is :  " + service_provider)

    result.insert(END, '\nStreet  :  ' + str(adrs.street))
    result.insert(END, '\nCity  :  ' + str(adrs.city))
    result.insert(END, "\nThe country of this number is :  " + location)
    result.insert(END, '\nPostal Code :  ' + str(adrs.postal))

helv14 = tkFont.Font(family="Helvetica", size=14, weight="bold")

lab1 = Label(text="Phone number Tracker", font=helv14)
lab1.pack()

number = Text(height=1)
number.pack()

button = ttk.Button(text="Search", bootstyle="info-outline", command=get_result)
button.pack(pady=10, padx=110)

result = Text(height=7)
result.pack()

app.mainloop()

