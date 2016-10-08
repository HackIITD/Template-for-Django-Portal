import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SearchApp.settings')
import django
django.setup()

from searchPokemon.models import pokedex
from searchPokemon.views import makelist

def large():
	resultarr = makelist()
	for eachPokemon in resultarr :
		add(Pokemon_name = eachPokemon["name"],Pokemon_Img_Url = eachPokemon["image_url"])

def add(Pokemon_name,Pokemon_Img_Url,Pokemon_type="N/A"):
	try:
		p = pokedex.objects.get_or_create(Pokemon_name = Pokemon_name,
        	Pokemon_Img_Url=Pokemon_Img_Url,
        	Pokemon_Type=Pokemon_type)[0]
		p.save()
	except:
		print "Data not saved Name :",Pokemon_name

large()