import requests
city_name = 'Bharatpur'
API_key = 'b7b9c50e7e349697f036bde778af76c2'
url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric'

response = requests.get(url)
if response.status_code ==200:
     data= response.json()
     print('weather is',data['weather'][0]['description'])
     print('Current Temperature is',data['main']['temp'])
     print('Current Humidity is',data['main']['humidity'])



