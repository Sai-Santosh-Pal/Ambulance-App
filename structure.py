class Location:
    def __init__(self):
        pass
    def find_coords(self):
        # importing geopy library
from geopy.geocoders import Nominatim
 
print("Latitude = ", getLoc.latitude, "\n")
print("Longitude = ", getLoc.longitude)


class ApiStructure:
    def __init__(self, location):
        self.location = location
