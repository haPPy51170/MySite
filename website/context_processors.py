from .models import SocialLink


def social_links(request):
    return {
        "sociallinks": SocialLink.objects.all()
    }