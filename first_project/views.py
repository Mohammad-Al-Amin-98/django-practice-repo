from django.http import HttpResponse
def home(request):
    return HttpResponse("This is my Home Page")

def about(request):
    return HttpResponse("This is my about page.")
