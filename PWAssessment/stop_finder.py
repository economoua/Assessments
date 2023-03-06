import requests
import json 
import string
from tkinter import *

class StopFinder:

    def __init__(self, root):
        self.root = root

#This function creates a new window to allow the user to either see all stops along a route after validation of input or if input 
# validation fails it allows the user to try again and refreshes a new window. With more time I would have changed this to 
# refreshing the same root window to update information rather than closing and opening a window each time. 
    def print_stops(self, route_value, header):

        top = Toplevel(self.root)
        top.geometry("450x450")
        top.title("Route Request")

        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)


        if self.scan_and_verify_input(route_value.get()) is False:
            stop_request=Label(top, text=route_value.get() + " was not a valid route. Try again", relief="solid", justify=CENTER)
            stop_request.pack()

            entryvalue = StringVar()

            entry = Entry(top, textvariable=entryvalue)
            entry.pack()

            search_button = Button(top, 
                text="Search Stops", 
                command=lambda: [self.print_stops(entryvalue, "All stops found on route \"" + entryvalue.get() + "\":\n"), top.destroy()])
            search_button.pack()
            exit_button = Button(top, text="Back", command=lambda: top.destroy())
            exit_button.pack()
        else: 
            response_stops = requests.get('https://api-v3.mbta.com/stops?filter[route]='+string.capwords(route_value.get()))
            stop_data = response_stops.text
            parsed_json = json.loads(stop_data)

            stop_list = Listbox(top)
            stop_list.config(width=400, height= 400, yscrollcommand = scrollbar.set)
            stop_list.insert(END, header)

            id_string = 'ID: '
            name_string = '  - NAME: '

            for each in parsed_json['data']:
                stop_list.insert(END, "\n")
                stop_list.insert(END, id_string + each['id'] + name_string + each['attributes']['name'])
                stop_list.insert(END, "Address: " + each['attributes']['address'])

            exit_button = Button(top, text="Back", command=lambda: top.destroy())
            exit_button.pack()
            stop_list.pack(side=LEFT, fill=BOTH)
            scrollbar.config(command = stop_list.yview)

#This function is for validation to verify the user entered an expected value in the 
# list of existing standard rail routes. Example: Red, Blue, Orange
# Currently not able to allow a user to search by the long name of a rail such as "Red Line", 
# though functionality would be possible to add through string transformations and another filter criteria.
# I would also like to make this more robust to take in comma seperated values to show more than one route at a time. 
    def scan_and_verify_input(self, user_entry):
        all_routes = requests.get('https://api-v3.mbta.com/routes?filter[type]=0,1')
        parsed_json = json.loads(all_routes.text)

        route_list = []

        for each in parsed_json['data']:
            route_list.append(each['id'])

        if string.capwords(user_entry) not in route_list:
            return False
        else:
            return True