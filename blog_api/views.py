from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import PostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from blog.models import Post
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["author"]
    search_fields = ['body']
    ordering_fields = '__all__'
    ordering = ['body']


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, )

class AllUsersView(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserPostView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.kwargs['id']
        return Post.objects.filter(author=user)


