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
# djaknas
# from geopy.geocoders import Nominatim
# loc = Nominatim(user_agent="GetLoc")

# class Location:
#     def __init__(self):
#         pass
#     def find_coords(self):
#         try:
#             return [getLoc.longitude, getLoc.longitude]
#         except Exception as e:
#             return e

# loc = Location()

# class ApiStructure:
#     def __init__(self, location=loc.find_coords()):
#         self.location = location
#     def get_coords(self):
#         print(self.location)
#         return self.location

# api = ApiStructure()
# api.get_coords()
# print("done")
import geocoder
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print(IPAddr)
g = geocoder.ip(IPAddr)
print(g.latlng)


# sadads

g = geocoder.ip('me')
g.address

# absa
# from geopy.geocoders import Nominatim
# loc = Nominatim(user_agent="GetLoc")

# class Location:
#     def __init__(self):
#         pass
#     def find_coords(self):
#         try:
#             return [getLoc.longitude, getLoc.longitude]
#         except Exception as e:
#             return e

# loc = Location()

# class ApiStructure:
#     def __init__(self, location=loc.find_coords()):
#         self.location = location
#     def get_coords(self):
#         print(self.location)
#         return self.location

# api = ApiStructure()
# api.get_coords()
# print("done")

# from geopy.geocoders import Nominatim

# def get_user_location():
#     try:
#         # Using 'ipinfo.io' as the geocoder
#         geolocator = Nominatim(user_agent="geoapiExercises", format_string="%s")
#         location = geolocator.geocode('')
        
#         # Extract location details
#         if location:
#             latitude = location.latitude
#             longitude = location.longitude
#             address = location.address
#             return {
#                 'latitude': latitude,
#                 'longitude': longitude,
#                 'address': address
#             }
#         else:
#             return None

#     except Exception as e:
#         print("Error occurred:", e)
#         return None

# if __name__ == "__main__":
#     user_location = get_user_location()
#     if user_location:
#         print("Latitude:", user_location['latitude'])
#         print("Longitude:", user_location['longitude'])
#         print("Address:", user_location['address'])
#     else:
#         print("Failed to retrieve the user's location.")

