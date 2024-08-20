from django.shortcuts import render
from .serializers import TaskSerializer
from .models import Task
from rest_framework import viewsets
from .tasks import add
from django.http import HttpResponse


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def my_view(request):
    # Запуск задачи Celery
    result = add.delay(10, 20)

    # Вернем клиенту ответ сразу, не дожидаясь завершения задачи
    return HttpResponse(f'Task ID {result.id}')
