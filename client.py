import requests

#data = {"Name":"Person X"} ## for post requests
response= requests.get("http://localhost:8000")
print(response.status_code)
print(response.text)
