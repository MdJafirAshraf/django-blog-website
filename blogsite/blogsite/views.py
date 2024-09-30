from django.template.loader import get_template
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    return HttpResponse("<h1>Lets Start the Django Project</h1>")

# example page for regression path
def re_page(request):
    return HttpResponse("<h1>Thisis the sample regression page.</h1>")

# example page for templates

def about_page (request):
    content  = "Hello! This is the about page"
    template_obj = get_template('about.html').render({"content": content})
    return HttpResponse(template_obj)

def contact_page (request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)

    template_name = 'contact.html'
    context = {"title": "Contact Us"}
    return render(request, template_name, context)