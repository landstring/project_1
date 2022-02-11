from django.shortcuts import render, redirect
from .models import Admins
import requests
from .forms import ObjectForm

def index(request):
    return render(request, 'main/index.html')

def buy(request): 
    if request.method == 'POST':
        form = ObjectForm(request.POST)
        object_name = form.data.get('object_name')
        object_place = form.data.get('object_place')
        notification('Покупка', object_name, object_place)
        return redirect('index')
    else:
        form = ObjectForm(None)
    return render(request, 'main/notification.html', {'form' : form})
    
def booking(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST)
        object_name = form.data.get('object_name')
        object_place = form.data.get('object_place')
        notification('Бронирование', object_name, object_place)
        return redirect('index')
    else:
        form = ObjectForm(None)
    return render(request, 'main/notification.html', {'form' : form})

def resume(request):
    if request.method == 'POST':
        form = ObjectForm(request.POST)
        object_name = form.data.get('object_name')
        object_place = form.data.get('object_place')
        notification('Резюме', object_name, object_place)
        return redirect('index')
    else:
        form = ObjectForm(None)
    return render(request, 'main/notification.html', {'form' : form})

def notification(event_type, object_name, object_place):
    if event_type == 'Покупка':
        users = Admins.objects.filter(type = "1")
    elif event_type == 'Бронирование':
        users = Admins.objects.filter(type = "2")
    elif event_type == 'Резюме':
        users = Admins.objects.filter(type = "3")
    
    for user in users: 
        text = 'Событие: ' + event_type + '\nОбъект: ' + object_name + '\nАдрес: ' + object_place
        telegram_url = 'https://api.telegram.org/bot1919759990:AAEEjyo9DLD8GwRiX8YCGMZxFVPLvh4TQAs/sendMessage?chat_id=' + user.telegram_id + '&text=' + text
        requests.get(telegram_url)
