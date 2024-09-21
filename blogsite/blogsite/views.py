from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Lets Start the Django Project</h1>")


# example page for regression path
def re_page(request):
    return HttpResponse("<h1>Thisis the sample regression page.</h1>")