from django.contrib import admin
from .models import Race, Route
from django.utils.text import Truncator


class RaceAdmin(admin.ModelAdmin):
   list_display   = ('name', 'city', 'postal_code','date_start','date_creation','description_truncated')
   list_filter    = ('name', 'city', 'postal_code','date_start','date_creation')
   date_hierarchy = 'date_creation'
   ordering       = ('date_creation', )
   search_fields  = ('name', 'city', 'postal_code','date_start','date_creation')

   def description_truncated(self,race):
   		return Truncator(race.description).chars(40, truncate='...')
    
   description_truncated.short_description = 'Description'

admin.site.register(Race, RaceAdmin)
admin.site.register(Route)
