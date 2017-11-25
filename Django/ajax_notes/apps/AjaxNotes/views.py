from django.shortcuts import render, redirect, HttpResponse
from .models import *


def index(request):
    notes = Note.objects.all()
    context = {
        "notes": notes
    }
    return render(request, 'AjaxNotes/index.html', context)

def add(request):
    title = request.POST['title']
    note = Note.objects.create(title=title, description="Enter a description here...")
    return HttpResponse(note.id)

def delete(request):
    note_id = request.POST['note_id']
    Note.objects.get(id=note_id).delete()
    return HttpResponse(True)

def update(request):
    note_id = request.POST['note_id']
    note = Note.objects.get(id=note_id)
    description = request.POST['description']
    print("Note id: "+note_id)
    print("Description: "+description)
    note.description = description
    note.save()
    return HttpResponse(True)
