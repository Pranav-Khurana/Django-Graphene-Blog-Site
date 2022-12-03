from django.db import models
from django.conf import settings

# Create your models here.
class userProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)

    def __str__(self):
        return self.user.get_username()

class tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class post(models.Model):
    class Meta:
        ordering = ["-publish_date"]
        unique_together = ("title", "author")
       
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(max_length=250, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(userProfile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(tag, blank=True)

