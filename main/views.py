from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Veronika",
        "npm": "2606816516",
        "study_program": "KKI Computer Science",
        "bio": (
            "A Computer Science exchange student at Universitas Indonesia for this semester."
            "I came from Russia and really appreciate this experience!"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Veronika",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

from main.models import Experience

