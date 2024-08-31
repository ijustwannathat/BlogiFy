from django.urls import path, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .views import PostList, PostDetail, AllUsersView, UserPostView


urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='post_list'),
    path('all_users/',AllUsersView.as_view(), name='all_users'),
    re_path(r'user/(?P<id>.+)/$', UserPostView.as_view(), name='user_post'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),


]