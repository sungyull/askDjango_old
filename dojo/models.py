# dojo/models.py

from django import forms
from django.db import models


def min_len_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력 요망!!!')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[min_len_3_validator])
    content = models.TextField()
    ip = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

