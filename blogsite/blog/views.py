from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.
def blog_post_details(request, slug):

    # obj = BlogPost.objects.filter(slug=slug).first()
    obj = get_object_or_404(BlogPost, slug=slug)

    template_name = "blog_post_details.html"
    context = {"blog": obj}

    return render(request, template_name, context)