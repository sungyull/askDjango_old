# blog/forms.py

from django import forms
from .models import Post

def min_len_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력 요망!!!')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

