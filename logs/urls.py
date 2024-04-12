from django.urls import path
from .views import logsList, logListByDocumento

urlpatterns = [
    path('logs/', logsList),
    path('logs/<int:documento>', logListByDocumento)
]
