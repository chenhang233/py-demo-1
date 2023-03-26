import requests

x = requests.get('https://www.runoob.com/')


print(x.text)