import requests

request = requests.get('https://bit.ly/3IqmZh3', allow_redirects=False)

if request.status_code == 301:
    print('RIGHT')
else:
    print('WRONG')