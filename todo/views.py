from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from todo.models import Tasks
from todo.serializers import TasksSerializer


class TasksView(ModelViewSet):
    queryset = Tasks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TasksSerializer
