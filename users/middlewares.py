from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class QualifSalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/'and request.method == 'POST':
            qualification = str(request.POST.get('qualification'))
            if qualification == "Junior":
                request.salary = 300
            elif qualification == "Middle":
                request.salary = 1000
            elif qualification == "Senior":
                request.salary = 2000
            else:
                return HttpResponseBadRequest('Вы не попадаете ни под одну квалификацию')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'salary', 'Зарплата не определена, проверьте данные еще раз!')
