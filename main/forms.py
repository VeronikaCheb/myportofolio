from django import forms
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags
from main.models import Project, Experience


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'category', 'is_completed']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Portfolio Website'}),
            'description': forms.Textarea(attrs={'placeholder': 'Tell us about your project', 'rows': 3}),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Project name can't contain only HTML tags.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()


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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Title can't contain only HTML tags.")
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()