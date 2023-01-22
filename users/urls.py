from django.urls import path, include
from rest_framework import routers
from .views import CustomUserViewSet,RegisterView

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
]