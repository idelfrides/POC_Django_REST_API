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
    data['wm'] = 'IDELFRIDES JORGE WM'
    data['title'] = 'Home | Django REST '
    return render(request, 'resthome.html', data)
