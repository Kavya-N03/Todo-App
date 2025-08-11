from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={
                'placeholder':'Enter your task...',
                 'class':'task-input'
            })
        }
        
