from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Part, Topics, Rooms


class RoomsForm(ModelForm):
    class Meta: 
        model = Rooms
        fields = "__all__"


class TopicsForm(ModelForm):

    class Meta:
        model = Topics
        fields = '__all__'