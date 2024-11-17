from datetime import datetime
from django.views import generic, View
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from main_page.models import Book


# book_list
class BookListView(generic.ListView):
    template_name = 'book.html'
    model = Book
    context_object_name = 'book_list'

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


# def book_list_view(request):
#     if request.method == 'GET':
#         books = Book.objects.filter().order_by('-id')
#         context = {'book_list': books}
#         return render(request, template_name="book.html", context=context)


# book_detail
class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    model = Book
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Book, id=book_id)


# def book_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(Book, id=id)
#         context = {'book_id': book_id}
#         return render(request, template_name="book_detail.html", context=context)


class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = 'book_list'
    paginate_by = 5

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get('q')).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class AboutMeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('First name: Esentur, Last name: Asankulov, Age: 17, Gender: Male')


# def about_me(request):
#     if request.method == 'GET':
#         return HttpResponse('First name: Esentur, Last name: Asankulov, Age: 17, Gender: Male')


class AboutMyPetsView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("My dog Charlie: <img src = 'https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg'  >")


# def about_my_pets(request):
#     if request.method == 'GET':
#         return HttpResponse("My dog Charlie: <img src = 'https://www.nylabone.com/-/media/project/oneweb/nylabone/images/dog101/10-intelligent-dog-breeds/golden-retriever-tongue-out.jpg'  >")


class SystemTimeView(View):
    def get(self, request, *args, **kwargs):
        time = datetime.now()
        return HttpResponse(f"Current time: {time}")


# def system_time(request):
#     if request.method == 'GET':
#         time = datetime.now()
#         return HttpResponse(f"Current time: {time}")
