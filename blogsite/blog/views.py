from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm

# Create your views here.

# blog list view
def blog_list_view(request):

    obj = BlogPost.objects.all()

    template_name = "blog_list_view.html"
    context = {"blogs": obj}

    return render(request, template_name, context)

# blog create view
def blog_create(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        
        # obj = BlogPost.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.slug = form.cleaned_data.get('slug') + "-blog"
        form.save()

        form = BlogPostModelForm()

    template_name = "form.html"
    context = {
        "title": 'Create New Blog',
        "form": form
        }

    return render(request, template_name, context)

# blog post detail view
def blog_post_details(request, slug):

    # obj = BlogPost.objects.filter(slug=slug).first()
    obj = get_object_or_404(BlogPost, slug=slug)

    template_name = "blog_post_details.html"
    context = {"blog": obj}

    return render(request, template_name, context)

# blog update view
def blog_update(request,slug):

    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()

    template_name = "form.html"
    context = {
        "title": f'Update {obj.title}',
        "form": form
        }

    return render(request, template_name, context)

# blog delete view
def blog_delete(request, slug):

    obj = get_object_or_404(BlogPost, slug=slug)

    template_name = "delete.html"
    if request.method == 'POST':
        obj.delete()
        return redirect('/blogpost')

    context = {"object": obj}

    return render(request, template_name, context)

