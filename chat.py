import tkinter
import folium
from tkinterwebview import TkinterWebView
from folium import IFrame
from io import BytesIO

def create_marker_with_label(map, location, label):
    html = f'<p>{label}</p>'
    iframe = IFrame(html=html, width=100, height=50)
    popup = folium.Popup(iframe, max_width=300)
    marker = folium.Marker(location=location, popup=popup)
    return marker

root_tk = tkinter.Tk()
root_tk.geometry("500x500")
root_tk.title("Maps")

# Create a folium map
map_object = folium.Map(location=[20, 0], zoom_start=3)

# Add markers with labels
marker1 = create_marker_with_label(map_object, [11.4064, 76.6932], "Location 1")
marker2 = create_marker_with_label(map_object, [20.5937, 78.9629], "Location 2")
marker3 = create_marker_with_label(map_object, [7.8731, 80.7718], "Location 3")

# Add markers to the map
map_object.add_child(marker1)
map_object.add_child(marker2)
map_object.add_child(marker3)

# Save the map as an HTML file
map_object.save("map.html")

# Create a TkinterWebView to display the map
web_view = TkinterWebView(root_tk, width=600, height=600)
web_view.load_url("map.html")
web_view.pack(fill="both", expand=True)

root_tk.mainloop()
