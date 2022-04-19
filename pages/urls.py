from django.urls import path
from .views import homepage, blog_detail, HomepageContent,BlogDetailView

urlpatterns = [
    path("", HomepageContent.as_view(), name="homepage"),
    path("blog/<slug:blog_slug>", BlogDetailView.as_view(), name="blog_detail"),
]
