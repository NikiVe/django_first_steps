from django.shortcuts import render

from app_01.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index.html', context)
