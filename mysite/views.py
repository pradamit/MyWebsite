from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import user_details, user_posts
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
import requests
from pytz import timezone, all_timezones
from datetime import datetime
# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print("returning FORWARDED_FOR")
        ip = x_forwarded_for.split(',')[-1].strip()
    elif request.META.get('HTTP_X_REAL_IP'):
        print("returning REAL_IP")
        ip = request.META.get('HTTP_X_REAL_IP')
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(f"returning REMOTE_ADDR is {ip}")
    return ip

def time_conversion(time_received):
    format = "%Y-%m-%d %H:%M:%S %p"
    processed_time = datetime.fromisoformat(time_received).astimezone(timezone('Asia/Kolkata')).strftime(format)
    return processed_time

def homepage(request):
    ip = get_client_ip(request)
    url_location = f'http://ip-api.com/json/?fields=country,regionName,city,lat,lon'
    location = requests.request("GET", url_location).json()
    lat = location['lat']
    lon = location['lon']
    url_sunset_sunrise = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={lon}&formatted=0'
    sunset_sunrise = requests.request("GET", url_sunset_sunrise).json()
    sunrise = time_conversion(sunset_sunrise['results']['sunrise'])
    sunset = time_conversion(sunset_sunrise['results']['sunset'])
    url_news = 'http://newsapi.org/v2/top-headlines?country=in&apiKey=13e3fa63f39f48948b97f3b0e19b52a6'
    news = requests.request("GET", url_news).json()
    articles = news['articles']
    lenght_of_news_list = len(articles)
    news_div = int(lenght_of_news_list/4)
    list_0 = articles[:4]
    list_1 = articles[4:8]
    list_2 = articles[8:12]
    list_3 = articles[12:16]
    list_4 = articles[16:20]
    #data = {'list_0':list_0,'list_1':list_1,'list_2':list_2,'list_3':list_3,'list_4':list_4}
    #data = [aa,bb,cc,dd,ee]
    context = {'location' : location,
               'sunrise':sunrise,
               'sunset':sunset,
               'lenght_of_news_list': lenght_of_news_list,
               'news_div':news_div,
               'data':[list_0,list_1,list_2,list_3,list_4],
               'list_0': list_0,'list_1': list_1, 'list_2': list_2, 'list_3': list_3, 'list_4': list_4
               }
    return render(request, 'mysite/homepage.html', context)

def posts(request):
    resp = user_posts.objects.filter(state='published').order_by('-date_posted')
    context = {'resp': resp}
    return render(request, 'mysite/posts.html', context)

def contacts(request):
    return render(request, 'mysite/contacts.html')

def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('username_entered')
        password = request.POST.get('password_entered')
        user_entered = authenticate(request, username=user_name, password=password)
        if user_entered:
            if user_entered.groups.first().name == 'APPROVER':
                return redirect('/login/approver/')
            else:
                login(request, user_entered)
                return redirect('/login/author/')
        else:
            return HttpResponse('User not found')
    else:
        return render(request, 'mysite/login.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email_id = request.POST.get('email_id')
        #password = request.POST.get('password')
        address_1 = request.POST.get('address_1')
        address_2 = request.POST.get('address_2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = float(request.POST.get('zip'))
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            username = new_user.cleaned_data.get('username')
            password = new_user.cleaned_data.get('password1')
            p = User.objects.create_user(username=username, password=password, email=email_id, first_name=fname, last_name=lname)
            p.save()
            n = user_details(first_name=fname,last_name=lname, email_id=email_id, address_1=address_1, address_2=address_2, state=state,
                         city=city, zip=zip)
            n.save()
            m = user_posts(author = n.first_name +' '+ n.last_name, user_id = p)
            m.save()
            messages.success(request, 'Hurray! Your account is created')
            return HttpResponseRedirect('/register/')
        else:
            messages.warning(request, str(new_user.errors))
            return render(request, 'mysite/register.html', {'form' : UserCreationForm})
    else:
        return render(request, 'mysite/register.html', {'form' : UserCreationForm})