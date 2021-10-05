from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Todo
from .serializers import TodoSerializer


class PostList(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
