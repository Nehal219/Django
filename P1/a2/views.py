from django.shortcuts import render, HttpResponse

def met(request):
    return HttpResponse("Kate Bush")

def met1(request):
    return render(request, 'tes.html', {'name':'hel'})