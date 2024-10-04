from django.shortcuts import render

# Create your views here.
import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city= request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + 
                                        city + '&units=metric&appid=b7b9c50e7e349697f036bde778af76c2').read()
        list_of_data =json.loads(source)

        data = {
            "temp" : str(list_of_data['main']['temp']) + '°C',
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : str(list_of_data['weather'][0]['icon']),

        }
        print(data)
    else:
        data ={}
    return render(request, "main/index.html", data)