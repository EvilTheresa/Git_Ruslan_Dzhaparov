from django import forms
from .models import Task, STATUS_CHOICES

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['description', 'status', 'due_date', 'details']
        widgets = {
            'status': forms.Select(choices=STATUS_CHOICES),
            'due_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'details': forms.Textarea(attrs={'rows':3, 'cols':25})
        }
