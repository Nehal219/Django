from django.shortcuts import HttpResponse, render
def m1(request):
    return HttpResponse("Scorched Earth")

def m2(request):
    return render(request, 'tes.html', {'name':'William Butcher'})