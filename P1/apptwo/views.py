from django.shortcuts import render

def app2(request):
    return render(request, 'tes.html',{'name':'Simon'})