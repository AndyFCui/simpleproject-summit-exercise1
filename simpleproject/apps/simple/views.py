from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>It works - Again!</h1>')

def hello(request):
    text = request.GET.get('text', 'everyone')

    return HttpResponse('<h1>Hello %s.</h1>' % text)
