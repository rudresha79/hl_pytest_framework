
import requests

end_point_url = 'https://todo.pixegami.io/'
response = requests.get(end_point_url)
print(response)
print(response.status_code)
data = response.json()
print(data)