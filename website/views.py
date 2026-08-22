from django.shortcuts import render
from website.models import (
    Profile,
    AboutCard,
    Skill,
    BlogPost,
    SocialLink,
    Headline,
    ContactMessage,
    Project,
)


def home_view(request):

    profile = Profile.objects.first()

    headlines = list(
        Headline.objects
        .order_by("order")
        .values_list("text", flat=True)
    )

    about_cards = AboutCard.objects.all().order_by("order")
    skills = Skill.objects.all()
    projects = Project.objects.all()
    blogposts = BlogPost.objects.all()
    sociallinks = SocialLink.objects.all()

    context = {
        "profile": profile,
        "headlines": headlines,
        "about_cards": about_cards,
        "skills": skills,
        "projects": projects,
        "blogposts": blogposts,
        "sociallinks": sociallinks,
    }

    return render(request, "home.html", context)


def test(request):
    return render(request, "index.html")