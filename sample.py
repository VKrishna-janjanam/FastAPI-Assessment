# testing the API
import requests

response = requests.post(url="http://localhost:8000/aircrafts", data={"name":"vamsi"})
print(response.json())