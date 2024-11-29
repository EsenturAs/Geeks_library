from django.views import generic
from . import models, forms
from django.http import HttpResponse


class RanobelibListView(generic.ListView):
    template_name = "ranobelib/ranobelib_list.html"
    context_object_name = "ranobelib_list"
    model = models.Ranobelib

    def get_queryset(self):
        return models.Ranobelib.objects.all().order_by("-id")


class RanobelibFormView(generic.FormView):
    template_name = "ranobelib/ranobelib_form.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse("200 OK")
        else:
            return super(RanobelibFormView, self).post(request, *args, **kwargs)
