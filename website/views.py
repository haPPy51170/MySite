from website.models import *
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404

def home_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "پیام شما با موفقیت ارسال شد.")
            return redirect(reverse("website:home") + "#contact")
    else:
        form = ContactForm()

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
        "form": form,
    }

    return render(request, "home.html", context)

def blog_detail(request, id=None, slug=None):

    if id is not None:
        blogpost = get_object_or_404(
            BlogPost,
            id=id
        )

    else:
        blogpost = get_object_or_404(
            BlogPost,
            slug=slug
        )

    return render(
        request,
        "blog_detail.html",
        {
            "blogpost": blogpost
        }
    )

