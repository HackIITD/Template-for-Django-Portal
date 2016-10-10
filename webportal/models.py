from django.db import models

# Create your models here.
class School(models.Model):
	points = models.IntegerField(default = 0)
	ranking = models.IntegerField(default = -1)             # -1 for no ranking 
	school_iD = models.CharField(max_length=128,unique = True)
	name = models.CharField(max_length=128)
	pincode = models.CharField(max_length=128)
	
	def __unicode__(self):
		return self.name

class Student(models.Model):
	profile_picture = models.CharField(max_length=128,blank = True)
	points = models.IntegerField(default = 0)
	ranking = models.IntegerField(default = -1)             # -1 for no ranking 
	student_iD = models.CharField(max_length=128,unique=True)
	fb_iD = models.CharField(max_length=128,blank = True)
	school_name = models.CharField(max_length=128)
	gender = models.CharField(max_length=128,blank = True)
	name = models.CharField(max_length=128)
	mobile_no = models.CharField(max_length=128)
	password = models.CharField(max_length=128)

	def __unicode__(self):
		return self.name

class Questions(models.Model):
	upvotes = models.IntegerField(default = 0)
	Ques = models.CharField(max_length=1024)
	ans = models.CharField(max_length=128)
	option1 = models.CharField(max_length=128)
	option2 = models.CharField(max_length=128)
	option3 = models.CharField(max_length=128)
	status = models.CharField(max_length=128,default='closed')   #after the competetion status gets equal to 'open'

	def __unicode__(self):
		return self.upvotes




