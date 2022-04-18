from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

""" Homepage Banner Model """
class HomepageBanner(models.Model):
    banner_title = models.CharField(max_length=200)
    banner_subtitle = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.id} | {self.banner_title}'

""" Homepage Blogs,Article page Blog and Blog detail page blog Model """
class Blog(models.Model):
    blog_image = models.ImageField(upload_to='images/')
    blog_title = models.CharField(max_length=250)
    blog_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=False)
    published = models.BooleanField(default=True)

    def __str__(self):
        return f'ID{self.id} | {self.blog_title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.blog_title)
        return super().save(*args, **kwargs)
    

