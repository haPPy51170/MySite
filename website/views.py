from django.shortcuts import render
from website.models import *


def home_view(request):
    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

    profile = Profile.objects.first()

    headlines = list(
        Headline.objects
        .order_by("order")
        .values_list("text", flat=True)
    )

    about_cards = AboutCard.objects.all().order_by("order")
    stats = Stat.objects.all().order_by("order")
    skills = Skill.objects.all()
    projects = Project.objects.all()
    blogposts = BlogPost.objects.all()
    sociallinks = SocialLink.objects.all()

    context = {
        "profile": profile,
        "headlines": headlines,
        "stats": stats,
        "about_cards": about_cards,
        "skills": skills,
        "projects": projects,
        "blogposts": blogposts,
        "sociallinks": sociallinks,
    }

    return render(request, "home.html", context)


def test(request):
    return render(request, "index.html")