from django.db import models

# Create your models here.
class pokedex(models.Model):
	Pokemon_name = models.CharField(max_length=128,unique = True)
	Pokemon_Img_Url = models.CharField(max_length=128,blank =True)
	Pokemon_Type = models.CharField(max_length=128,blank = True)

	def __unicode__(self):
		return self.Pokemon_name