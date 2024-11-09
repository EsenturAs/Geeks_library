from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from main_page.models import Book, ReviewBooks


# book_list
def book_list_view(request):
    if request.method == 'GET':
        books = Book.objects.filter().order_by('-id')
        context = {'book_list': books}
        return render(request, template_name="book.html", context=context)


# book_detail
def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Book, id=id)
        context = {'book_id': book_id}
        return render(request, template_name="book_detail.html", context=context)


def about_me(request):
    if request.method == 'GET':
        return HttpResponse('First name: Esentur, Last name: Asankulov, Age: 17, Gender: Male')


def about_my_pets(request):
    if request.method == 'GET':
        return HttpResponse(
            "My dog Charlie: <img src = 'https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg'  >")


def system_time(request):
    if request.method == 'GET':
        time = datetime.now()
        return HttpResponse(f"Current time: {time}")
