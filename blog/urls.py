from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import BlogViewSet, get_user_info, register_user, get_my_blogs, login_view

router = DefaultRouter()
router.register(r'blog', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path('me/', get_user_info),
    path('users/', register_user),
    path('my-blogs/', get_my_blogs),
    path('login/', login_view, name='login'),
    path('api/public-blogs/', views.public_blogs),
    # Signup
]
