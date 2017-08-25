# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from random import randint
from fusion import *
# Create your views here.

def index(request):
    if 'id' in request.session:
        request.session['id'] = None
    return render(request, 'yelp_api_test/index.html')  

def login(request):
    pass

def register(request):
    pass

def logout(request):
    return redirect('/')  

def home(request):
    return render(request, 'yelp_api_test/home.html')  

def add_friends(request):
    if request.method == 'POST':
        request.session['group_fb_ids'] = request.POST['group_fb_ids']
        print request.session['group_fb_ids']
    return redirect('/categories')  

def categories(request):    
    return render(request, 'yelp_api_test/categories.html')

def process(request):
    if request.method == 'POST':
        if not request.POST['location_input']:
            return redirect('/categories')
        else:
            arr= request.POST.getlist('category')
            filters= ','.join(arr)
            print filters
            # request.session['search'] = request.POST['search']
            request.session['location_input'] = request.POST['location_input']
            request.session['search_results'] = query_api(filters, request.session['location_input'])
            return redirect('/results')
    else:
        return redirect('/home')

def results(request):
    search_results = request.session['search_results']
    random=randint(1,20)
    print random
    search_results=search_results['businesses'][random]
    context = {
        'places': search_results
    }

    print search_results
    return render(request, 'yelp_api_test/home.html', context)

def goback(request):
    return redirect('/home')