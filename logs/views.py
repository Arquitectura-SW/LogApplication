from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .serializer import LogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .logic.logic_logs import getLogs, getLogsByDocumento

@api_view(['GET'])

def logsList(request):
    if request == 'GET':
        try:
            logs = getLogs()
            serializer = LogSerializer(logs, many= True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": "The logs wasn't found."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])     
def logListByDocumento(request, document):
    if request == 'GET':
        try:
            logs = getLogsByDocumento(document)
            serialiazer = LogSerializer(logs, many=True)
            return Response(serialiazer.data)
        except Exception as e:
            return Response({"error": "The logs wasn't found."}, status=status.HTTP_400_BAD_REQUEST)


