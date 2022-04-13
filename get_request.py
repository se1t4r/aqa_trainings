import requests

request = requests.get('https://github.com/')

if request.status_code == 200:
    print('OK')
else:
    print('NOT OK')

# just comment for update