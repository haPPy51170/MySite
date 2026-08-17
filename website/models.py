from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50)
    headline = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    # image
    def __str__(self):
        return f"{self.id}. {self.name}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()

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

