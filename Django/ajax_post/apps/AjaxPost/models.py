from __future__ import unicode_literals
from django.db import models

class NoteManager(models.Manager):
    def add_note(self, postData):
        print("Note: "+postData['note'])
        return self.create(note=postData['note'])

class Note(models.Model):
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = NoteManager()
