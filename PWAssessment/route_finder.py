import requests
import json 
from tkinter import *

class RouteFinder:

    def __init__(self, root):
        self.root = root

#This function allows for the user to interact with buttons off of the root window and get a printed list 
# of all routes that exist for each transportation category. It is currently set up with 'magic numbers'
# on the buttons that correspond with the API documentation, though I would have liked to dive into the API documentation
# more to discover if there is a value I could use from there to prevent any complications down the road if those numerical values are reassigned.
    def print_routes(self, route_numbers, header):
        top = Toplevel(self.root)
        top.geometry("450x450")
        top.title("Route Request")

        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)

        response_stops = requests.get('https://api-v3.mbta.com/routes?filter[type]='+route_numbers)
        stop_data = response_stops.text
        parsed_json = json.loads(stop_data)

        route_list = Listbox(top)
        route_list.config(width=400, height= 400, yscrollcommand = scrollbar.set)
        route_list.insert(END, header)

        id_string = 'ID: '
        name_string = '  - NAME: '

        for each in parsed_json['data']:
            route_list.insert(END, "\n")
            route_list.insert(END, id_string + each['id'] + name_string + each['attributes']['long_name'])

        exit_button = Button(top, text="Back", command=lambda: top.destroy())
        exit_button.pack()
        route_list.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command = route_list.yview)