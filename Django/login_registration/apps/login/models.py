from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')


class UserManager(models.Manager):
    def validate_login(self, post_data):
        errors = []
        if len(self.filter(email = post_data['email'])) > 0:
            user = self.filter(email = post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('Password is incorrect')
        else:
            errors.append('Email and/or password incorrect')
        if errors:
            return errors
        return user

    def validate_registration(self, post_data):
        errors = []
        #names
        if len(post_data['first_name'])<2 or len(post_data['last_name'])<2:
            errors.append("First/last name must be at least 2 characters")

        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append("Name's must only contain letters")

        #email
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("Invalid email")

        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("Email already in use")

        #pw
        if len(post_data['password'])<8:
            errors.append("Password must contain at least 8 characters.")

        if post_data['confirm_password'] != post_data['password']:
            errors.append("Passwords do not match.")

        if not errors:
            
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))

            new_user = self.create(
                first_name = post_data['first_name'],
                last_name = post_data ['last_name'],
                email = post_data ['email'],
                password = hashed
            )
            return new_user
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 255)
    objects = UserManager()
    def __str__(self):
        return self.email
