from django.urls import path
from .views import user_id

urlpatterns = [
    path('user-id/', user_id, name='user_id'),
]