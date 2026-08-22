from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Profile(models.Model):
    name_fa = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    bio_fa = models.TextField()
    bio_en = models.TextField()
    status_fa = models.CharField(max_length=100, blank=True)
    status_en = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    location = models.CharField(max_length=100, blank=True)
    # role = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image

class Headline(models.Model):
    text = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

class Stat(models.Model):
    value = models.CharField(max_length=20)
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

class AboutCard(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100),
        ]
    )

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # image
    tag = models.CharField(max_length=100)
    url = models.URLField()

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    excerpt = models.TextField()
    published_at = models.DateTimeField()

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SocialLink(models.Model):
    platform = models.CharField(max_length=100)
    url = models.URLField()
    icon = models.CharField(max_length=100)

