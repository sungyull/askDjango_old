# dojo/forms.py

from django import forms
from .models import Post, GameUser


def min_len_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError('3글자 이상 입력 요망!!!')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user_agent' ]
        widgets = {
            'user_agent': forms.HiddenInput,
        }


class GameUserForm(forms.ModelForm):
    class Meta:
        model = GameUser
        fields = ['server_name', 'username']

    def clean_username(self):
        return self.cleaned_data.get('username', '').split()



# class PostForm(forms.Form):
#     title = forms.CharField(validators=[min_len_3_validator])
#     content = forms.CharField(widget=forms.Textarea())
#
#     def save(self, commit=True):
#         post = Post(**self.cleaned_data)
#         if commit:
#             post.save()
#         return post




