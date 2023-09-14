import requests

resp = requests.get("http://www.google.com")


print(resp.text)
#print(requests.__version__)