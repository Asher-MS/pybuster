import requests

url="https://asher-ms.github.io"

resp=requests.get(url)
print(resp.status_code)
