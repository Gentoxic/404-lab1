import requests

resp = requests.get("https://raw.githubusercontent.com/Gentoxic/404-lab1/master/lab1.py")


print(resp.text)
#print(requests.__version__)