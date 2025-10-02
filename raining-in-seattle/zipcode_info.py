import urllib.parse, urllib.request, urllib.error, json
class Place:
    def __init__(self, lat, lon, name, state):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.state = state

def zipcode_info(countrycode, zipcode):
    url = "https://api.zippopotam.us/" + countrycode + "/" + str(zipcode)
    with urllib.request.urlopen(url) as response:
        return response.read().decode()

country = "US"
zip = 98105
print(zipcode_info(country, zip))