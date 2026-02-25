from django.shortcuts import render # type: ignore


from django.http import HttpResponse # type: ignore

def index3(request):
    return HttpResponse("User Module Works!")
