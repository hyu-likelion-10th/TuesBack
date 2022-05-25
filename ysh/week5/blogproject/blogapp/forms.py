from dataclasses import fields
from turtle import title
from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
      #입력 받고자 하는 값들
      title = forms.CharField()
      body = forms.CharField(widget=forms.Textarea)


class BlogModelForm(forms.ModelForm):
      class Meta:
            model = Blog
            fields = '__all__' #전체 필드에 대해서 입력 받고 싶은 경우
            # fields = ['title', 'body']

class CommentForm(forms.ModelForm):
      class Meta:
            model = Comment
            # fields = '__all__' #전체 필드에 대해서 입력 받고 싶은 경우
            fields = ['comment']
