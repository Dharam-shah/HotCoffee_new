from statistics import mode
from django.shortcuts import render
from pages.models import HomepageBanner,Blog
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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
        homepage_banner_content = HomepageBanner.objects.first()
        context['banner_title'] = homepage_banner_content.banner_title if homepage_banner_content else None
        context['banner_subtitle'] = homepage_banner_content.banner_subtitle if homepage_banner_content else None
        context['banner_image'] = homepage_banner_content.banner_image if homepage_banner_content else None

        """ section First Blog """
        # homepage_blog_section1 = Blog.objects.get(id=1)
        # context['blog_title'] = homepage_blog_section1.blog_title
        # context['description'] = homepage_blog_section1.description
        # context['blog_date'] = homepage_blog_section1.blog_date
        context['hm_blog_sec1'] = Blog.objects.get(id=1)
        
        """ section Second Blog """
        #context['latest_blog'] = Blog.objects.all()[1:4]
        context['latest_blog'] = Blog.objects.filter(published=True).order_by('-blog_date')[:3]

        """ section Last Blog """
        context['hm_blog_last'] = Blog.objects.get(id=5)

        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog_detail'
    slug_url_kwarg = 'blog_slug'