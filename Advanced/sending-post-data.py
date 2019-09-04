# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://www.yoursite.com"

# data to be sent to api
data = {'log': 'admin',
        'pwd': '12345'
        }

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)
