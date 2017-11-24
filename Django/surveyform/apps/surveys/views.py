
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render (request, "surveys/index.html")

def process_form(request):
    try:
        request.session['submissions']
    except KeyError:
        request.session['submissions'] = 0
    request.session['submissions'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect("/results")

def display_result(request):
    return render (request, 'surveys/results.html')
