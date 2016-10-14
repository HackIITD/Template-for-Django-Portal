from django.shortcuts import render,redirect
from django.http import HttpResponse
from webportal.models import Student,School
from random import random
import urllib2 , datetime
from google import search
from bs4 import BeautifulSoup as BS 
import json, requests, random, re 
from pprint import pprint
from math import floor
from webportal.randomprofile import randomProfile


def index(request):

	if request.method =='POST':
		mode = request.GET.get("method")
		if(mode == "signin"):
			print "'''''\n----19------\n'''''\n"
			try:
				mobile_number = request.POST.get("mobile_number")
				password = request.POST.get("password")
				print mobile_number
				print password
				print Student.objects.all()
				for x in Student.objects.all():
					print x.name + x.mobile_no
					if mobile_number == x.mobile_no and password == x.password :
						print "Matched"
						return render(request,"webportal/mainpage.html",{"user_name":x.name.split(" ")[0],"mobile_number":mobile_number,"error":None,"signin":0})
				context = json.dumps({"sigin":1})		
				print context
				return render(request,"webportal/account.html",{"signin":1})
			except :
				context = json.dumps({"sigin":1})		
				print context
				return render(request,"webportal/account.html",{"signin":1})
		elif mode == "signup":
			try:
				print "''''\nGot here --22---\n'''''\n"
				first_name = request.POST.get("first_name").encode("utf-8")
				print first_name +"\n"
				last_name = request.POST.get("last_name").encode("utf-8")
				print last_name +'\n'
				school_name = request.POST.get("school_name").encode("utf-8").lower()
				print school_name + '\n'
				pincode = request.POST.get("pincode").encode("utf-8")
				print pincode + '\n'
				mobile_number = request.POST.get("mobile_number").encode("utf-8")
				print mobile_number +'\n'
				password = request.POST.get("password").encode("utf-8")
				print password +'\n'
				status = json.loads(addStudent(first_name+" "+last_name,mobile_number,school_name,pincode,password))
				print status["status"]
				if status["status"] == 200 :
					return render(request,"webportal/mainpage.html",{"user_name":first_name,"mobile_number":mobile_number,"error":None})
				elif status["status"] == 403:
					return render(request,"webportal/account.html",{"error":"This portal is not working properly please try after sometime"})

			except:
				print "''''''\n----35----\n''''''"
				return render(request,"webportal/account.html",{"error":"This portal is not working properly please try after sometime"})

	return render(request,"webportal/mainpage.html",{"data":[None]})

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
		context = {"status":200,"data":result_arr}
		return 	context
	except:
		context = {"status":403,"data":[None]}
		return context

def addStudent(name,mobile_no,school_name,pincode,password):
	print "\n Called addStudent() ----73----- \n"
	student_iD = school_name.lower()[0:2] + pincode + '_' + mobile_no
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
			p = Student.objects.get_or_create(student_iD = student_iD,mobile_no=mobile_no,
								name=name,password=password,school_name=school_name
								,profile_picture=profile_picture)[0]
			print "-----88----\n"
			p.save()
			print "saved"
			context = json.dumps({"status":200,"report":"Saved successfully"})
			print context
			return context
		except:
			print "Data not saved \n" , Student.objects.all()
	except Exception as e:
		print "\n''''' Error : " + e + "\n  -------85------- \n"
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

def date(string):
	dateobject = datetime.datetime.strptime(string,"%Y-%m-%d %H:%M")
	return dateobject

def quesarena(request):
	q=Questions.objects.all()
	d={}
	result_arr = []
	# d['questions'] = q
	for ques in q:
		r=[ques.ans,ques.option1,ques.option2,ques.option3]
		shuffle(r)
		result_arr.append(r)
	d['list']=zip(result_arr,q)
	print "result_arr**************", result_arr
	print "****list*******" , d['list']
	return render(request, "webportal/qarena.html", d)

def addques(request):
	d={}
	return render(request , 'webportal/addques.html',d)

def createevent(request):
	d={}
	return render(request, 'webportal/createevent.html', d)

def api(request,api_call):
	api = {}
	if api_call.lower() == "users":
		api["data"] = []
		try:
			for x in Student.objects.all():
				add={}
				add["name"] = x.name.decode("utf-8");
				print "name added"
				add["school_name"] = x.school_name.decode("utf-8")
				print "school_name added"
				add["student_id"] = x.student_iD.decode("utf-8")
				add["password"] = x.password.decode("utf-8")
				add["mobile_no"] = x.mobile_no.decode("utf-8")
				add["ranking"] = x.ranking
				add["points"] = x.points
				try:
					api["data"].append(add)
					print "appended"
				except:
					print "it didnt worked"	
			api["status"] = 200
			return HttpResponse(json.dumps(api)) 
		except:
			api["status"] = 404
			api["data"] = [None]
			return HttpResponse(json.dumps(api))
	else :
		return HttpResponse(json.dumps({"status":404,"data":[None]}))				

def event(request):
	print "I got the call"
	context_dict = {}
	if request.method == "POST":
		mobile_number = request.POST.get("mobile_number")
		print mobile_number
		for x in Student.objects.all():
			print x
			if x.mobile_no == mobile_number:
				context_dict["name"] = x.name.decode("utf-8")
				print "name saved"
				context_dict["school_name"] = x.school_name.decode("utf-8")
				print "schoolname saved"
				context_dict["student_iD"] = x.student_iD.decode("utf-8")
				print "studentiD saved"
				context_dict["profile_picture"] = x.profile_picture.decode("utf-8")
				print "Profile picture saved"
				context_dict["ranking"] = x.ranking
				print "ranking saved"
				context_dict["points"] = x.points
				print "points saved"
				try:
					print "tryin to render"
					return HttpResponse(json.dumps(context_dict))
				except :
					print "failed"
					return HttpResponse(json.dumps({"status":"Kamyaaabi"}))
	if request.method == "GET":
		a = request.GET.get("z")
		if request.GET.get("z") :
			for x in Student.objects.all():
				if x.student_iD == a :
					context_dict["profile_picture"] = request.GET.get("profile_picture")
					print context_dict["profile_picture"]
					context_dict["name"] = request.GET.get("name")
					context_dict["points"] = request.GET.get("points")
					context_dict["school_name"] = request.GET.get("school_name")
					try:
						context_dict["status"] = 200
					except:
						context_dict["status"] = 404
					return render(request,"webportal/create_event.html",context_dict)
		return redirect("/")