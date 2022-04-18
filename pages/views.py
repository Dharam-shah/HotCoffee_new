from django.shortcuts import render
from pages.models import HomepageBanner,Blog
from django.views.generic.list import ListView
# Create your views here.

def homepage(request):
    #return HttpResponse("Homepage")
    return render(request, "pages/homepage.html")

def blog_detail(request):
    return render(request, "blogs/blog_detail.html")

""" Homepage Banner Views """
# class HomepageBannerContent(TemplateView):
#     template_name = 'pages/homepage.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         homepage_banner_data = Homepage_banner.objects.get(id=1)
#         context = {
#             'Banner_title': homepage_banner_data.Banner_title,
#             'Banner_subtitle': homepage_banner_data.Banner_subtitle,
#             'Banner_image': homepage_banner_data.Banner_image, 
#         }
#         return context

""" Homepage Blogs Views """
class HomepageContent(ListView):
    model = Blog
    template_name = 'pages/homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        homepage_banner_content = HomepageBanner.objects.get(id=1)
        context['banner_title'] = homepage_banner_content.banner_title
        context['banner_subtitle'] = homepage_banner_content.banner_subtitle
        context['banner_image'] = homepage_banner_content.banner_image

        homepage_blog_section1 = Blog.objects.get(id=1)
        context['blog_title'] = homepage_blog_section1.blog_title
        context['description'] = homepage_blog_section1.description
        context['blog_date'] = homepage_blog_section1.blog_date

        return context