import tkinter as tk
from tk_tools import map_label

# Define a list of locations
locations = [
    {"name": "Location 1", "latitude": 12.9715987, "longitude": 77.5945627},
    {"name": "Location 2", "latitude": 13.0827, "longitude": 80.2707},
    # Add more locations here
]

# Create a tkinter window
root = tk.Tk()
root.title("Pin Map")

# Create a MapLabel widget to display the map
map_label = MapLabel(root, width=600, height=400)
map_label.pack()

# Iterate over the list of locations
for location in locations:
    # Pin the location on the map
    pin = map_label.create_oval(location["longitude"] - 0.005, location["latitude"] - 0.005,
                                 location["longitude"] + 0.005, location["latitude"] + 0.005,
                                 fill="red", outline="red")

    # Label the place
    text = map_label.create_text(location["longitude"] - 5, location["latitude"] - 5,
                                 text=location["name"], fill="black", font=("Arial", 12, "bold"))

# Start the tkinter main loop
root.mainloop()