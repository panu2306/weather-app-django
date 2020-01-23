import requests
from django.shortcuts import render

from .models import City

# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=32be061454a4b28a2121d983fd704d94'
    city = 'bangalore'

    r = requests.get(url.format(city)).json()
    
    cities = City.objects.all()
    
    weather_data = []

    for city in cities:
        city_weather = {
            'city' : city.name,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
    
        weather_data.append(city_weather) 
    
    print(weather_data)
    context = {'weather_data' : weather_data}
    return render(request, 'weather/weather.html', context=context)