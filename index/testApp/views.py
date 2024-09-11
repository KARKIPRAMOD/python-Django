from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable': 
        "this is sent"
    }
    return render(request,'index.html', context)
    # return HttpResponse('THIS IS HOME PAGE')

def about(request):
    return HttpResponse('THIS IS ABOUT PAGE')

def services(request):
    return HttpResponse("THIS IS SERVICES PAGE")

def contat(request):
    return HttpResponse("THIS IS CONTACT")