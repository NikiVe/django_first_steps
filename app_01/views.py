from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

from app_01.forms import TodoForm
from app_01.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
        'todo_form': TodoForm(),
    }
    return render(request, 'index.html', context)


@require_POST
def create_todo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        return HttpResponse('Done')
