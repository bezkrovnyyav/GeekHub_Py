from django.shortcuts import render
from django.http import HttpResponse
from.models import Askstories, Jobstories, Showstories, Newstories
import requests

def index(request):
    return render(request, 'homework/index.html')


def proccess(name):
    response = requests.get(f'https://hacker-news.firebaseio.com/v0/{name}.json?print=pretty')
    text = response.json()
    all_list = list()
    for id in text:
        response_id = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json?print=pretty')
        json = response_id.json()
        if json != None:
            all_list.append(json)
    return all_list


def askstories(request):
    for json in proccess('askstories'):
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
    return HttpResponse('Askstories done')


def showstories(request):
    for json in proccess('showstories'):
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
    return HttpResponse('Showstories done')


def jobstories(request):
    for json in proccess('jobstories'):
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
    return HttpResponse('Jobstories done')


def newstories(request):
    for json in proccess('newstories'):
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
    return HttpResponse('Newstories done')