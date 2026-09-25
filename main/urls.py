from django.urls import path
from main.views import (
    show_main,
    show_experience,
    create_experience,
    update_experience,
    delete_experience,
    get_experience_json,
    show_project,
    create_project,
    update_project,
    delete_project,
    get_projects_json,
    register,
    login_user,
    logout_user,
    toggle_star,
    toggle_star_experience,
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:experience_id>/update/", update_experience, name="update_experience"),
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("project/", show_project, name="show_project"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/<uuid:project_id>/update/", update_project, name="update_project"),
    path("projects/<uuid:project_id>/delete/", delete_project, name="delete_project"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star,name="toggle_star",),
    path("experience/<uuid:experience_id>/star",toggle_star_experience,name="toggle_star_experience"),
]