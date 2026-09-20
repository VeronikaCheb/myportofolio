from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm


def show_main(request):
    context = {
        "name": "Veronika",
        "npm": "2606816516",
        "study_program": "KKI Computer Science",
        "bio": (
            "A Computer Science exchange student at Universitas Indonesia for this semester. "
            "I came from Russia and really appreciate this experience!"
        ),
    }
    return render(request, "index.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)
    data = serializers.serialize("json", experiences)
    return HttpResponse(data, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize(
        "json", json_response.content.decode("utf-8")
    )
    experiences = [e.object for e in experiences]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Veronika",
        "experience_list": experiences,
        "title_query": title_query,
    }
    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New experience added!")
        return redirect("main:show_experience")

    context = {"name": "Veronika", "form": form}
    return render(request, "experience_form.html", context)

def update_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)
    form = ExperienceForm(request.POST or None, instance=experience)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience updated!")
        return redirect("main:show_experience")

    context = {"name": "Veronika", "form": form, "experience": experience}
    return render(request, "experience_form.html", context)

def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience deleted!")
    return redirect("main:show_experience")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()
    if title_query:
        projects = projects.filter(title__icontains=title_query)
    data = serializers.serialize("json", projects)
    return HttpResponse(data, content_type="application/json")

def show_project(request):
    json_response = get_projects_json(request)
    projects = serializers.deserialize(
        "json", json_response.content.decode("utf-8")
    )
    projects = [p.object for p in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Veronika",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project added!")
        return redirect("main:show_project")

    context = {"name": "Veronika", "form": form}
    return render(request, "projects_form.html", context)

def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Project updated!")
        return redirect("main:show_project")

    context = {"name": "Veronika", "form": form, "project": project}
    return render(request, "projects_form.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted!")
    return redirect("main:show_project")