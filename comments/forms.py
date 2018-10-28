#!/usr/bin/env python
# encoding: utf-8

from .models import Comment
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class CommentForm(ModelForm):
    url = forms.URLField(
        label='网址',
        required=False,
        widget=forms.URLInput(
            attrs={
                'class': 'form-control com_input',
                'placeholder': "请输入网址",
            }
        )

    )
    email = forms.EmailField(
        label='电子邮箱',
        required=True,
    )
    name = forms.CharField(
        label='姓名', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control com_input',
                'value': "",
                'size': "30",
                'maxlength': "245",
                'aria-required': 'true'
            }
        )
    )
    parent_comment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control com_input',
                'placeholder': '我来评两句~',
                'rows': 5,
                'style':'max-width:100%',
                'required':"内容不能为空",
            }),
        }