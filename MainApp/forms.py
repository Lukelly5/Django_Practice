from django import forms

from .models import *

class TopicForm(forms.ModelForm):
    class Meta: # meta class tells Django which model to base the form on and which fields to include in the form
        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Type something here...'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}