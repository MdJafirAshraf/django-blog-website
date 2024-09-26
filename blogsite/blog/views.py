from django.shortcuts import render, get_object_or_404
from .models import BlogPost

# Create your views here.

# blog list view
def blog_list_view(request):

    obj = BlogPost.objects.all()

    template_name = "blog_list_view.html"
    context = {"blogs": obj}

    return render(request, template_name, context)

# blog create view
def blog_create(request):

    obj = BlogPost.objects.all()

    template_name = "blog_create.html"
    context = {"blog": obj}

    return render(request, template_name, context)

# blog post detail view
def blog_post_details(request, slug):

    # obj = BlogPost.objects.filter(slug=slug).first()
    obj = get_object_or_404(BlogPost, slug=slug)

    template_name = "blog_post_details.html"
    context = {"blog": obj}

    return render(request, template_name, context)

# blog update view
def blog_update(request):

    obj = BlogPost.objects.all()

    template_name = "blog_update.html"
    context = {"blog": obj}

    return render(request, template_name, context)

# blog delete view
def blog_delete(request):

    obj = BlogPost.objects.all()

    template_name = "blog_delete.html"
    context = {"blog": obj}

    return render(request, template_name, context)

