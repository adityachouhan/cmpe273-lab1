import requests

def dateFunc():
  r = requests.get('https://webhook.site/f377a059-1c83-4ebd-80ce-007de6067d25')
  print(r.headers['Date'])

dateFunc()
dateFunc()
dateFunc()