from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router_v1 = DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='posts')
router_v1.register(r'groups', GroupViewSet, basename='groups')
router_v1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(
        'v1/posts/<int:post_pk>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='post_comments_list_create'
    ),
    path(
        'v1/posts/<int:post_pk>/comments/<int:pk>/',
        CommentViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy'
        }),
        name='post_comment_detail'
    ),
    path('v1/jwt/create/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
