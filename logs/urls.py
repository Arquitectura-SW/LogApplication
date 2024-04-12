from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import logsList, logsListDocumento

urlpatterns = [
    path('logs/', logsList),
    path('logs/<int:documento>', logsListDocumento)
]
