from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'./first_app/home.html',{"name":"I am Fahim","marks":86,"courses":[
        {
            "id": 1,
            "course":"C",
            "teacher":"Fahim"
            },
        {
            "id":2,
            "course":"C++",
            "teacher":"Faria"
            },
        {
            "id":3,
            "course":"Python",
            "teacher":"Taha"
            }
        ]})

def about(request):
    return render(request,'./first_app/about.html',{"author":"glenn Maxwell"})
