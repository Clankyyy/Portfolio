from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Project
from django.http import HttpResponse
from django.views.generic.list import ListView


def index(request):
    return HttpResponse("Hello, world. You're at the portfolio index.")


class ProjectList(ListView):
    model = Project
    template_name = "portfolio/index.html"
    context_object_name = "projects"

    def get_queryset(self) -> QuerySet[Any]:
        return Project.objects.all()
