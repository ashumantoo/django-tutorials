from datetime import datetime

from django.shortcuts import render


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


# Create your views here.
def basic_concept(request):
    context = {
        "name": "John Doe",
        "age": 35,
        "skills": ["Python", "Django", "FastApi"],
        "user": User("Mark", "mark@gmail.com"),
        "blog": {
            "title": "Django Template concept",
            "content": "<b> This is bold content </b>",
            "created_at": datetime(2026, 7, 1)
        },
        "empty_value": None
    }
    return render(request, 'basic-concepts.html', context)


def template_filters(request):
    post = {
        "title": "Django: A new generation framework",
        "description": "Django is a high level python web framework, which uses MVT pattern.",
        "author": None,
        "comments_count": 10,
        "created_at": datetime(2026, 7, 1),
        "tags": ['Python', 'Django', 'Web Framework', 'Full Stack Development'],
        "float_value": 54.2334
    }
    context = {
        "post": post
    }
    return render(request, 'filters-in-django-template.html', context)


def template_conditionals(request):
    posts = [
        {
            "title": "The Hidden Cost of AI Agents: What CFOs Need to Know",
            "description": "AI agents are no longer a future investment. In 2026, they have become a budget item, and CFOs are being asked to approve them faster than finance teams can evaluate them.",
            "author": "John Doe",
            "is_featured": False,
            "created_at": datetime(2026, 7, 1)
        },
        {
            "title": "Power BI May 2026: New AI & Dashboard Enhancements",
            "description": "If you work with data, build dashboards, or just rely on Power BI to make sense of your numbers, then May 2026 is a release worth reading about. Microsoft has packed in meaningful upgrades this month, and the best part? Most of them are built to make your day-to-day work noticeably easier.",
            "author": "Micky Watson",
            "is_featured": False,
            "created_at": datetime(2026, 7, 1)
        },
        {
            "title": "60+ Brilliant App Ideas for Startups to Launch in 2026",
            "description": "If you work with data, build dashboards, or just rely on Power BI to make sense of your numbers, then May 2026 is a release worth reading about. Microsoft has packed in meaningful upgrades this month, and the best part? Most of them are built to make your day-to-day work noticeably easier.",
            "author": "Adam Jackson",
            "is_featured": True,
            "created_at": datetime(2026, 7, 1)
        }
    ]

    context = {
        "posts": posts,
        "today": datetime.now(),
        "html_code":"<b>Welcome To The Blog</b>"
    }
    return render(request, 'conditionals.html', context)
