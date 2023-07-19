from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request,'./first_app/index.html',{
        "name":"I am Abdur Rahim", "marks": 86, "lst":[24,3,10,5], "blog":"First of all, I am a fierce fighter in in this world. Rarely I can accomodate myself with the peoples of this world. So it's hard for me in this world."
        })
