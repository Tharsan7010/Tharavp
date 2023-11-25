import tkinter as tk
from tkinter import ttk
import folium
from folium.plugins import MarkerCluster
import webbrowser
import os

class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Map with Pins")

        # Create a Tkinter map frame
        self.map_frame = ttk.Frame(root)
        self.map_frame.pack(fill="both", expand=True)

        # Create a map using Folium
        self.mymap = folium.Map(location=[11.1132540432738, 77.34730968962972], zoom_start=10)

        # Create a MarkerCluster to group pins
        self.marker_cluster = MarkerCluster().add_to(self.mymap)

        # Add some sample pins
        self.add_pin(11.134948832762781, 77.34040734711846, "Tiruppur new bus stand","20")
        self.add_pin(11.126487227675971, 77.36490383069008, "MGR Colony","15")
        self.add_pin(11.135627687984591, 77.3285775181773, "Gandhinagar","10")

        # Convert the map to HTML
        self.html_file = "map.html"
        self.mymap.save(self.html_file)

        # Create a button to open the map in a web browser
        open_button = ttk.Button(root, text="Open Map", command=self.open_in_browser)
        open_button.pack()

    def add_pin(self, lat, lon, popup_text,label):
        # Add a pin to the map
        folium.Marker([lat, lon], popup=popup_text, tooltip=label).add_to(self.marker_cluster)

    def open_in_browser(self):
        # Open the generated HTML file in a web browser
        webbrowser.open("file://" + os.path.abspath(self.html_file))

if __name__ == "__main__":
    root = tk.Tk()
    app = MapApp(root)
    root.mainloop()
