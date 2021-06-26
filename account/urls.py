from django.urls import path
from .views import registration

urlpatterns = [
    path('api/register/', registration, name='register')
]