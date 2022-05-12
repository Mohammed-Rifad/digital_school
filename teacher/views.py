from django.http import JsonResponse
from django.shortcuts import render

from .models import *

# Create your views here.


def auth_check(request):
     
    params=request.data
    statusCode=0
    email=params['email']
    passwd=params['passwd']
    try:
        login_check=Teacher.objects.get(email=email,password=passwd)
        statusCode=200
    except:
        statusCode=401
    return JsonResponse({'statusCode':statusCode})
