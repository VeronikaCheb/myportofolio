from django import forms
from main.models import Project, Experience


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

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'description', 'category', 'thumbnail', 'ended_at']
        labels = {
            'title': 'Role / Position',
            'description': 'What did you do?',
            'category': 'Category',
            'thumbnail': 'Thumbnail URL',
            'ended_at': 'End date (leave empty if ongoing)',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'President of Student Council'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe what you did', 'rows': 3}),
            'category': forms.Select(),
            'thumbnail': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'ended_at': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }        