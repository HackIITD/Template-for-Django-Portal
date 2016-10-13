import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','portal_template.settings')
import django
django.setup()

from webportal.randomprofile import randomProfile
from webportal.models import Student


def add():
	try:
		student_iD = "2342384y8238"
		mobile_no ="323227498"
		name = "vaibhav"
		password = "dsjnjsd"
		school_name = "asdbada"
		profile_picture = randomProfile()
		points = 0
		ranking = -1
		fb_iD = "N/A"
		gender = "N/A"
		p = Student.objects.get_or_create(student_iD = student_iD,mobile_no=mobile_no,
					name=name,password=password,school_name=school_name
					,fb_iD=fb_iD,profile_picture=profile_picture)[0]
		p.save()
		print "Data saved for :" ,Student.objects.all() 
		print "\n" + p.name 

	except:
		print "Data not saved Name :", Student.objects.all()

def showDB():
	for pokemon in Student.objects.all():
		print pokemon.mobile_no		

def addStudent(name,mobile_no,school_name,pincode,password):
	print "\n Called addStudent() ----73----- \n"
	student_iD = school_name.lower()[0:2] + pincode + '_' + mobile_no
	print student_iD
	print type(student_iD)
	print type(mobile_no)
	print type(school_name)
	print type(pincode)
	print type(password)
	points = 0
	ranking = -1
	profile_picture = randomProfile()
	print profile_picture + '\n'
	try:
		print "Trying for saving"
		try:
			print "hello"
			p = Student.objects.get_or_create(fb_iD="N/A",student_iD=student_iD,mobile_no=mobile_no,name=name,password=password,school_name=school_name,profile_picture=profile_picture)[0]
			print "-----88----\n"
			p.save()
			print "saved"
			context = {"status":200,"report":"Saved successfully"}
			print context
		except:
			print "Data not saved \n" , Student.objects.all()
			context = {"status":403,"report":"Data not saved"}
			print context

	except Exception as e:
		print "\n''''' Error : " + e + "\n  -------85------- \n"
		context = {"status":403,"report":"Data not saved"}
		return context

# addStudent("vaibhav","9990274709","DTU","7213812","86328")
showDB()