from django.urls import path, include
from rest_framework import routers
from .views import CustomUserViewSet,RegisterView, ProfileUpdate

router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path("update/<int:pk>/", ProfileUpdate.as_view(), name="ProfileUpdate"),
                                           
]