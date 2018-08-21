from django.http import HttpResponseRedirect

from django.shortcuts import render

from .models import Uzer


def list(request):
    users = Uzer.objects.all()

    return render(request, 'usermanager/list.html', {'users': users})

def create(request):
    name = request.POST['name']
    phone = request.POST['phone']

    Uzer.objects.create(
        name=name,
        phone=phone,
    )

    return HttpResponseRedirect('list')
