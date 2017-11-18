from rest_framework.views import APIView
from rest_framework.response import Response

from todoapp.models import ToDoElement
from todoapp.serializers import ToDoSerializer


class ToDoView(APIView):
    def get(self, request):
        todos = ToDoElement.objects.all()
        serializer = ToDoSerializer(todos, many=True)
        return Response(serializer.data)
