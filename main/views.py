from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import datetime
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied 

from main.models import Experience, Project
from main.forms import ProjectForm, ExperienceForm


# def show_main(request):
#     context = {
#         "name": "Veronika",
#         "npm": "2606816516",
#         "study_program": "KKI Computer Science",
#         "bio": (
#             "A Computer Science exchange student at Universitas Indonesia for this semester. "
#             "I came from Russia and really appreciate this experience!"
#         ),
#     }
#     return render(request, "index.html", context)

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    context = {
        "name": "Veronika Chebotareva",
        "npm": "2606816516",
        "study_program": "KI Computer Science",
        "bio": (
            "A Computer Science exchange student at Universitas Indonesia for this semester. "
            "I came from Russia and really appreciate this experience!"
        ),
        "last_login": last_login,
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
    projects_json = serializers.serialize(
        "json", projects, use_natural_foreign_keys=True
    )
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

@login_required(login_url="/login/")
def create_project(request):
    if not request.user.is_superuser:
        raise PermissionDenied

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

@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not request.user.is_superuser:
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project deleted!")
    return redirect("main:show_project")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Veronika",
        "form": form,
    }
    return render(request, "register.html", context)

# def login_user(request):
#     form = AuthenticationForm(request, data=request.POST or None)

#     if request.method == "POST" and form.is_valid():
#         login(request, form.get_user())
#         return redirect("main:show_main")

#     context = {
#         "name": "Veronika",
#         "form": form,
#     }
#     return render(request, "login.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Veronika",
        "form": form,
    }
    return render(request, "login.html", context)

# def logout_user(request):
#     logout(request)
#     return redirect("main:show_main")

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        # If this account has already starred it, remove the star.
        # If not, add one.
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)

    return redirect("main:show_projects")