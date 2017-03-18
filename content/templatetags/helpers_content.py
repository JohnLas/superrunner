from django import template

register = template.Library()

@register.filter
def get_race_name(value):
	switcher = {
        21097: "Semi-Marathon",
        42195: "Marathon",
    }
	return switcher.get(value, str(round(value/1000))+"K")