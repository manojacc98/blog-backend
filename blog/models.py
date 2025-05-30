
from django.db import models
from django.contrib.auth.models import AbstractUser
from markdownx.models import MarkdownxField


class AppUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = MarkdownxField()
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='blogs')
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title