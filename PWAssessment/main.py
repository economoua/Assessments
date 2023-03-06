# main.py
from route_finder import RouteFinder
from stop_finder import StopFinder
from tkinter import *

#Small little function to clear default input when the user goes to type in the stop search.
def clear(*args):
    entry.delete(0, "end")

root = Tk()
root.title("Travel Finder")
root.geometry("250x300")

route_finder = RouteFinder(root)

stop_finder = StopFinder(root)

# This is all the set up on the root tkinter to display labels/buttons. I would have prefered to set it up where these buttons refresh the main
# root rather than opening new frames in new windows, but with time constraints I went with the method I knew.
ok=Label(root, text="Press a button to see all associated lines:", relief="solid", justify=CENTER)
ok.grid(row=1,column=1, pady=5, padx=20)
ok.columnconfigure(1, weight=1)

button_rails = Button(root, text="Standard Rail Routes", command=lambda: route_finder.print_routes("0,1", "All Standard Rails:\n"))
button_rails.grid(row=2, column=1, pady=3)

button_commuter_rails = Button(root, text="Commuter Rail Routes", command=lambda: route_finder.print_routes("2", "All Commuter Rails:\n"))
button_commuter_rails.grid(row=3, column=1, pady=3)

button_bus = Button(root, text="Bus Routes", command=lambda: route_finder.print_routes("3", "All Bus Routes:\n"))
button_bus.grid(row=4, column=1, pady=3)

button_ferry = Button(root, text="Ferry Routes", command=lambda: route_finder.print_routes("4", "All Ferry Routes:\n"))
button_ferry.grid(row=5, column=1, pady=3)

stop_request=Label(root, text="Enter a standard rail route to see all stops:", relief="solid", justify=CENTER)
stop_request.grid(row=8,column=1, pady=10)

entryvalue = StringVar()
text_box_placeholder = "Enter Text: Ex. Red"
entry = Entry(root, textvariable=entryvalue)
entry.insert(0, text_box_placeholder)
entry.grid(row=10, column=1)

entry.bind("<FocusIn>", clear)

search_button = Button(root, text="Search Stops", command=lambda: stop_finder.print_stops(entryvalue, "All stops found on route \"" + entryvalue.get() + "\":\n"))
search_button.grid(row=11, column=1, pady=3)


exit_button = Button(root, text="Exit", command=lambda: root.destroy())
exit_button.grid(row=13, column=1, pady=10)

root.mainloop()
