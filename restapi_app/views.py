from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
import json, os

"""
 --------------------------------------------
   views methods begin from here 
 -------------------------------------------
"""

def resthome(request):
    data = {}
    data['title'] = 'Home | Django REST API '
    data['wm'] = 'IDELFRIDES JORGE'
    data['desc'] = 'This project make a POC of Django REST framework.'
    data['verb'] = 'POST'
    return render(request, 'resthome.html', data)


"""
    POST
    GET
    PUT
    PATH
    DELETE
"""