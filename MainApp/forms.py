from django import forms

from .models import *

class TopicForm(forms.ModelForm):
    class Meta: # meta class tells Django which model to base the form on and which fields to include in the form
        model = Topic
        fields = ['name', 'description']
        labels = {'text':''}