from django.http import HttpResponse
from django.shortcuts import render
from content.models import Race


# Create your views here.

def race(request,id_race=1):
	race = Race.objects.filter(id=id_race)[0]
	routes = race.route_set.all()
	return render(request, 'content/race.html', {'race': race, 'routes':routes})

def races(request):
	races = Race.objects.all()
	return render(request, 'content/races.html', {'races': races})


def map(request):
	return render(request, 'content/includes/map/map.html')

