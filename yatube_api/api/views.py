from rest_framework import viewsets, permissions, pagination, filters
from django.shortcuts import get_object_or_404

from posts.models import Post, Comment, Group, Follow
from .serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_post_object(self):
        post_id = self.kwargs.get('post_pk')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post_object()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post_object()
        serializer.save(author=self.request.user, post=post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['following__username', 'user__username']

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
