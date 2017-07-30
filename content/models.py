# -*- coding: utf-8 -*-

from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    facebook_page_url = models.URLField(max_length=1000,default="")
    description = models.CharField(max_length=10000)
    date_start = models.DateTimeField(auto_now_add=False, auto_now=False)
    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modidification = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.name+" "+self.city+" "+str(self.date_start)

class Route(models.Model): 
	distance_meter = models.IntegerField()
	max_runner_number = models.IntegerField()
	max_time = models.IntegerField()
	price = models.FloatField()
	race = models.ForeignKey('Race')
	path_url = models.URLField(max_length=1000)
	date_start = models.DateTimeField(auto_now_add=False, auto_now=False)

	def __str__(self):
		return str(self.distance_meter)+" "+self.race.name+" "+self.race.city+" "+str(self.date_start)