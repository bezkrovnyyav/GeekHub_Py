from django.shortcuts import render
from.models import Askstories, Jobstories, Showstories, Newstories
import requests


def index(request):
    value = request.POST.get('news_category')
    if value == 'new':
        new()
    elif value == 'ask':
        ask()
    elif value == 'show':
        show()
    elif value == 'job':
        job()
    return render(request, 'homework/index.html')


def proccess(name, list_id):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/{name}.json?print=pretty')
    text = response.json()
    all_list = list()
    for id in text:
        if id not in list_id:
            response_id = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
            json = response_id.json()
            if json != None:
                all_list.append(json)
    return all_list

def ask():
    list_id = Askstories.objects.all().values_list('id', flat=True)
    for json in proccess('askstories', list_id):
        try:
            table = Askstories.objects.create(
                by=json['by'],
                descendants=json['descendants'],
                id=json['id'],
                kids=json.get('kids', ''),
                score=json['score'],
                text=json.get('text', ''),
                time=json['time'],
                title=json['title'],
                type=json['type']
            )
            table.save()
        except:
            print('Exist')


def show():
    list_id = Showstories.objects.all().values_list('id', flat=True)
    for json in proccess('showstories', list_id):
        try:
            table = Showstories.objects.create(
                by=json['by'],
                descendants=json.get('descendants', ''),
                id=json['id'],
                kids=json.get('kids', ''),
                score=json.get('score', ''),
                text=json.get('text', ''),
                time=json['time'],
                title=json['title'],
                type=json['type'],
                url=json.get('url', '')
            )
            table.save()
        except:
            print('Exist')


def job():
    list_id = Jobstories.objects.all().values_list('id', flat=True)
    for json in proccess('jobstories', list_id):
        try:
            table = Jobstories.objects.create(
                by=json['by'],
                id=json['id'],
                score=json.get('score', ''),
                text=json.get('text', ''),
                time=json['time'],
                title=json['title'],
                type=json['type'],
                url=json.get('url', '')
            )
            table.save()
        except:
            print('Exist')


def new():
    list_id = Newstories.objects.all().values_list('id', flat=True)
    for json in proccess('newstories', list_id):
        try:
            table = Newstories.objects.create(
                by=json['by'],
                descendants=json['descendants'],
                id=json['id'],
                kids=json.get('kids', ''),
                score=json['score'],
                time=json['time'],
                title=json['title'],
                type=json['type'],
                url=json.get('url', ''),
                text=json['text']
            )
            table.save()
        except:
            print('Exist')