import uuid

from django.contrib.auth.models import User
from django.db import models


class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ("internship", "Internship"),
        ("research", "Research"),
        ("volunteer", "Volunteer"),
        ("part-time", "Part-Time"),
        ("full-time", "Full-Time"),
        ("freelance", "Freelance"),
        ("organizer", "Main Organizer"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default="full-time",
    )
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(
        User, related_name="starred_experiences", blank=True
    )
    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None

class Project(models.Model):
    PROJECT_CHOICES = [
         ("app", "Application Prototype"),
         ("ecology", "Ecology Project"),
         ("science", "Science Research"),
         ("ml", "Machine Learning Research"),
    ]  

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(
        max_length=20, 
        choices=PROJECT_CHOICES, 
        default='app'
    )
    thumbnail = models.URLField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    starred_by = models.ManyToManyField(
        User, related_name="starred_projects", blank=True
    )
    def __str__(self):
        return self.title