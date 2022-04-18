import requests
from getpass import getpass

response = requests.get('https://www.google.com/')
print(response)
print(type(response))
print(response.status_code)
for url in ['https://www.google.com', 'instagram.com']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except:
        print('Error')

response = requests.get('https://api.intra.42.fr')
print(response.headers)
data = response.json()
print(data)
# auth_response = requests.get('https://api.github.com/user', auth=('razdva0', getpass()))
# with requests.session() as session:
#    session.auth = ('razdva0', getpass())
#    response = session.get("https://api.github.com/user")
# print(response.json())
from requests.adapters import HTTPAdapter

adapter = HTTPAdapter(max_retries=3)
with requests.session() as session:
    session.mount("https://api.github.com/", adapter)
    session.auth = ("razdva0", getpass())

    try:
        session.get("https://api.github.com/user")
    except ConnectionError as err:
        print(f'Failed to connect: {err}')
    else:
        print('OK')