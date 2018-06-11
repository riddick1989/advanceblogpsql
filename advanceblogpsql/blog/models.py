from django.db import models
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
    updated = models.DateTimeField(auto_now=False,auto_now_add=True)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs:post-detail',kwargs={"id":self.id})