from django.contrib import admin
from .models import HomepageBanner, Blog

# Register your models here.

admin.site.register(HomepageBanner)
#admin.site.register(Blog)

class BlogSlug(admin.ModelAdmin):
    list_display = ("id", "blog_title", "blog_date",)
    prepopulated_fields = {"slug": ("blog_title",)} 

admin.site.register(Blog, BlogSlug)
