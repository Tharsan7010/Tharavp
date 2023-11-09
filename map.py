import tkinter

from tkintermapview import TkinterMapView

root_tk = tkinter.Tk()

root_tk.geometry("500x500")

root_tk.title("Thar Project")

map_widget = TkinterMapView(root_tk,width=600,height=400,corner_radius=0)

map_widget.pack(fill="both",expand=True)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
max_zoom=22)

marker1 = Marker(
    latitude=40.7128,  # Latitude for the first pin
    longitude=-74.0060,  # Longitude for the first pin
    label="Marker 1",
    icon="blue-dot.png"  # Optional: You can provide a custom icon image
)

marker2 = Marker(
    latitude=34.0522,  # Latitude for the second pin
    longitude=-118.2437,  # Longitude for the second pin
    label="Marker 2",
    icon="red-dot.png"  # Optional: You can provide a custom icon image
)
map_view.add_marker(marker1)
map_view.add_marker(marker2)

root_tk.mainloop()
