from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('First name: Esentur, Last name: Asankulov, Age: 17, Gender: Male')


def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse("My dog Charlie: <img src = 'https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg'  >")


def system_time(request):
    if request.method == 'GET':
        time = datetime.now()
        return HttpResponse(f"Current time: {time}")
