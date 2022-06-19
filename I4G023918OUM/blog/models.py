from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = get_user_model()
    Created_Date = models.DateTimeField(auto_now_add=True)
    Published_Date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['Created_Date']

        def __unicode__(self):
            return self.title
    