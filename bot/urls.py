from django.urls import path
from .views.webhook import webhook

urlpatterns = [
    path('webhook/', webhook, name='webhook'),
]