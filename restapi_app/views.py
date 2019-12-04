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
    data['wm'] = 'IDELFRIDES JORGE | War Machine Never Give Up'
    data['desc'] = 'This is project make a proof of concept to django REST framework.'
    data['title'] = 'Home | Django REST API '
    data['verb'] = ''
    return render(request, 'resthome.html', data)


"""
    POST
    GET
    PUT
    PATH
    DELETE
"""