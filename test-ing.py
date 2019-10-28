# importing the requests library
import requests

# api-endpoint
URL = "https://api.ing.com"


# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': 'abc'}

# sending get request and saving the response as response object
r = requests.post(URL+"/oauth2/token", params=PARAMS)


# extracting data in json format
data = r.json()


