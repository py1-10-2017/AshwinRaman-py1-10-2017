from __future__ import unicode_literals
from django.shortcuts import render, redirect
from time import strftime, gmtime

def index(request):
    if 'word_list' in request.session:
        context = {'words': request.session['word_list']}
        return render (request, 'session_app/index.html', context)
    else:
        request.session['word_list'] = []
        return render(request, 'session_app/index.html')

def create(request):
    if "font" not in request.POST:
        font = None
    else:
        font = request.POST['font']
    entry = {"word": request.POST['word'],
            "color": request.POST['color'],
            "font": font,'time':strftime("%A %B %d, %Y\n%H:%M %p", gmtime())}
    words = request.session['word_list']
    words.append(entry)
    request.session['word_list'] = words
    return redirect('/')

def clear(request):
    del request.session['word_list']
    return redirect('/')
