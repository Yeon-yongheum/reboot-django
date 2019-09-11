from django.shortcuts import render, redirect
from .models import Pastlife
from faker import Faker
import requests
from decouple import config
# Create your views here.

def index(request):
    return render(request, 'pastlifes/index.html')

def new(request):
    return render(request, 'pastlifes/new.html')

def result(request):
    name = request.GET.get('name')
    tmp = Pastlife.objects.filter(name=name)
    # 이름이 있으면
    if tmp:
        pastlife = Pastlife.objects.get(pk=tmp[0].pk)
    # 이름이 없으면
    else:
        fake = Faker('ko_KR')
        job = fake.job()
        pastlife = Pastlife.objects.create(name = name, job = job)
    # 직업 결과에 따라 giphy 요청
    job = pastlife.job
    api_key = 'QZg9Qr2JhwJFgKoB5lhOA2MqIWMhYCB2'
    # 1. url 설정
    url = f'http://api.giphy.com/v1/gifs/search?api_key={ api_key }&q={ job }&lang=ko'
    # 2. 요청 보내기
    response = requests.get(url).json()
    # 3. 응답 결과에서 이미지 url 뽑기
    try:
        image_url = response['data'][0].get('images').get('original').get('url')
    except:
        image_url = None
    context = {
        'pastlife' : pastlife,
        'image_url' : image_url
    }
    return render(request, 'pastlifes/result.html', context)


