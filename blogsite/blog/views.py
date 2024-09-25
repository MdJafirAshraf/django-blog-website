from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blog_post_details(request, post_id):

    obj = BlogPost.objects.get(id=post_id)

    template_name = "blog_post_details.html"
    context = {"blog": obj}

    return render(request, template_name, context)