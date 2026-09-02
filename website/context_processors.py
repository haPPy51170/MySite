from .models import Profile, SocialLink


def global_data(request):
    return {
        "profile": Profile.objects.first(),
        "sociallink": SocialLink.objects.all(),
    }
