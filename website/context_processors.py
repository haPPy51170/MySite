from .models import Profile, SocialLink


def global_data(request):
    return {
        "profile": Profile.objects.first(),
        "sociallinks": SocialLink.objects.all(),
    }
