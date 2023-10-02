from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method== 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=c801265f3f22a06ab552e76c3592aa41').read()
        json_data = json.loads(res)
        a=round(json_data['main']['temp']-273.5,2)
        b=str(a)
        data = {
            "city": city,
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temp": b + '°',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),

        }
    else:
        data ={}
    return render(request,'index.html', data)