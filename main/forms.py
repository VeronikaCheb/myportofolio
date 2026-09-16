from django import forms
from main.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'is_completed']
        labels = {
            'title': 'Project Title',
            'description': 'Description',
            'category': 'Category',
            'is_completed': 'Is Completed',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Portfolio Website',
                'maxlength': 255,
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Tell us about your project',
                'rows': 3,
            }),
            'category': forms.Select(attrs={}),
            'is_completed': forms.CheckboxInput(attrs={}),
        }