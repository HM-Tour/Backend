from django.urls import path
from .views import CurrentUserView

urlpatterns = [
    path('current_user', CurrentUserView.as_view(), name='current_user'),
    # other urls
]