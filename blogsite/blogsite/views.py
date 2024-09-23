from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return HttpResponse("<h1>Lets Start the Django Project</h1>")

# example page for regression path
def re_page(request):
    return HttpResponse("<h1>Thisis the sample regression page.</h1>")

# example page for templates
def temp_page (request):
    content  = "Hello! This is the sample template in django with context."
    return render(request, 'index.html', {"content": content})

def about_page (request):
    content  = "Hello! This is the about page"
    template_obj = get_template('about.html').render({"content": content})
    return HttpResponse(template_obj)