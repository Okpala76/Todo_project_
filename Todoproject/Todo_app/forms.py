from django import forms
from .models import TodoTask

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = ['title', 'description']


