import tkinter as tk
from tkinter import filedialog
import folium
import webbrowser
def create_map():
    m = folium.Map(location=[latitude, longitude], zoom_start=13)
    folium.Marker([latitude, longitude], popup=location_name).add_to(m)
    m.save('map.html')
    return 'map.html'
def open_map(file_path):
    url = 'file://' + file_path
    webbrowser.open_new_tab(url)

def create_map():
    m = folium.Map(location=[latitude, longitude], zoom_start=13)
    folium.Marker([latitude, longitude], popup=location_name).add_to(m)
    m.save('map.html')
    return 'map.html'

def open_map(file_path):
    url = 'file://' + file_path
    webbrowser.open_new_tab(url)

root = tk.Tk()
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=20)

label_latitude = tk.Label(frame, text="Latitude:")
label_latitude.grid(row=0, column=0)

entry_latitude = tk.Entry(frame)
entry_latitude.grid(row=0, column=1)

label_longitude = tk.Label(frame, text="Longitude:")
label_longitude.grid(row=1, column=0)

entry_longitude = tk.Entry(frame)
entry_longitude.grid(row=1, column=1)

label_location_name = tk.Label(frame, text="Location Name:")
label_location_name.grid(row=2, column=0)

entry_location_name = tk.Entry(frame)
entry_location_name.grid(row=2, column=1)

def retrieve_input():
    global latitude, longitude, location_name
    latitude = float(entry_latitude.get())
    longitude = float(entry_longitude.get())
    location_name = entry_location_name.get()

def on_map_click():
    retrieve_input()
    file_path = create_map()
    open_map(file_path)

button = tk.Button(root, text="Create Map", command=on_map_click)
button.pack(pady=10)

root.mainloop()