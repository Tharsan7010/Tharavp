import tkinter

from tkintermapview import TkinterMapView

root_tk = tkinter.Tk()

root_tk.geometry("1000x1000")
root_tk.title("Maps")

map_widget = TkinterMapView(root_tk,width=600,height=600
,corner_radius=0)

map_widget.pack(fill="both",expand=True)

map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
max_zoom=22)

map_widget.set_address("Goa",marker=True)
map_widget.set_address("Andhra Pradesh",marker=True)
map_widget.set_address("Karnataka",marker=True)
map_widget.set_address("Kerala",marker=True)
map_widget.set_address("Tamil Nadu",marker=True)
map_widget.set_address("Gujarat",marker=True)
map_widget.set_address("Rajasthan",marker=True)



root_tk.mainloop()  
