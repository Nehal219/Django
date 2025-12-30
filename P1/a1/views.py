from django.shortcuts import render, HttpResponse

# Create your views here.
def met(request):
    return HttpResponse("There's a fire")