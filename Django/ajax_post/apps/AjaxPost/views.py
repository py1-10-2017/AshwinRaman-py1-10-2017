from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    notes = Note.objects.all()
    context = {
        "notes": notes
    }
    return render(request, 'AjaxPost/index.html', context)

def add_note(request):

    Note.objects.add_note(request.POST)
    return HttpResponse(request.POST["note"])
