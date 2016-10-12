from django.shortcuts import render 
from django.http import HttpResponse
from webportal.models import Student,School
from random import random
import urllib2 , datetime
from google import search
from bs4 import BeautifulSoup as BS 
import json, requests, random, re
from pprint import pprint
from math import floor

def index(request):

	return render(request,"webportal/base.html",{"data":[None]})

def account(request):

	return render(request,"webportal/account.html",{"data":[None]})	

def Student_Rank():
	result_arr = []
	arr = Student.objects.all()
	arr.sort(key=lambda x : x.points)
	try:
		for a in range(0,3):
			result_arr.append(json.dumps({"name":a.name,"profile":a.profile_picture,"points":a.points}))	
		context = {"status":"200","data":result_arr}
		return 	context
	except:
		context = {"status":"403","data":[None]}
		return context

def School_Rank():
	result_arr = []
	arr = School.objects.all()
	arr.sort(key=lambda x : x.points)
	try:
		for a in range(0,3):
			result_arr.append(json.dumps({"name":a.name,"profile":a.profile_picture,"points":a.points}))	
		context = {"status":"200","data":result_arr}
		return 	context
	except:
		context = {"status":"403","data":[None]}
		return context

def addStudent(name,mobile_number,school_name,pincode,password):
	school_iD = school_name.lower()[0:2] + pincode + '_' + mobile_number
	points = 0
	ranking = -1
	try:
		p = Student.objects.get_or_create(student_iD = student_iD,mobile_number=mobile_number,
			name=name,password=password,school_name=school_name,points=points,ranking=ranking)[0]
		p.save()
		context = {"status":200,"report":"Saved successfully"}
		return context
	except:
		context = {"status":403,"report":"Data not saved"}
		return context

def addSchool(name,pincode):
	school_iD = school_name.lower()[0:2] + pincode 
	points = 0
	ranking = -1
	try:
		p = School.objects.get_or_create(school_iD = school_iD,pincode=pincode,
			name=name,points=points,ranking=ranking)[0]
		p.save()
		context = {"status":200,"report":"Saved successfully"}
		return context
	except:
		context = {"status":403,"report":"Data not saved"}
		return context

def randomProfile():
	Profile_picture=["https://help.github.com/assets/images/help/profile/identicon.png","https://github.com/identicons/jasonlong.png","https://raw.githubusercontent.com/sehrgut/node-retricon/master/examples/images/github.png","https://avatars2.githubusercontent.com/u/163800"]
	a = floor(random()*len(Profile_picture))
	profile = Profile_picture[int(a)]
	return profile

def date(string):
	dateobject = datetime.datetime.strptime(string,"%Y-%m-%d %H:%M")
	return dateobject
