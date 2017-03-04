from django.db import models

class Runner(models.Model):
    firstname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=200)
    sex = models.CharField(max_length=1)
    birthdate = models.DateTimeField(auto_now_add=False, auto_now=False)
    date_creation = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modidification = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.firstname+" "+self.name


class Race(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    distance_meter = models.IntegerField()
    max_runner_number = models.IntegerField()
    max_time = models.IntegerField()
    price = models.FloatField()
    path_url = models.CharField(max_length=1000)
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