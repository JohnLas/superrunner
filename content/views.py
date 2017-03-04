from django.http import HttpResponse
from django.shortcuts import render
from content.models import Runner
from content.models import Race


# Create your views here.

def home(request):
	text = "<h1>Hello super Runner</h1>"
	return HttpResponse(text)

def race(request,id_race=1):
	race = Race.objects.filter(id=id_race)[0]
	return render(request, 'content/race.html', {'race': race})

def races(request):
	races = Race.objects.all() 
	return render(request, 'content/races.html', {'races': races})

def edition(request,id_race=1,id_edition=1):
	text = "<h1>Edition "+id_edition+"</h1>"
	return HttpResponse(text)

def runner(request,id_runner=1):
	return render(request, 'content/runner.html', {'id_runner': id_runner})

def runners(request):
	runners = Runner.objects.all() 
	return render(request, 'content/runners.html', {'runners': runners})

def chrono(request, id_chrono=1):
	text = "<h1>Chrono "+id_chrono+"</h1>"
	return HttpResponse(text)