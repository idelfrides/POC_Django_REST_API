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
    data['desc'] = 'This is a Prove of concept to Django REST API'
    data['title'] = 'Home | Django REST API '
    return render(request, 'resthome.html', data)
