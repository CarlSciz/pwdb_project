from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")

def wrestler_by_id(request, wrestler_id):
    wrestler = Wrestler.objects.get(pk=wrestler_id)
    return render(request, 'wrestler_details.html', {"wrestler":wrestler})