from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from details import *
import requests, json

VERIFY_TOKEN = verify_token
PAGE_ACCESS_TOKEN = page_access_token

def index(request):
	greeting()
	domain_whitelist()
	set_menu()
	return HttpResponse(post_fb_msg('12','yo'))
	# return HttpResponse(handle_postback('12','something'))
	# return HttpResponse(greeting('12'))

def logg(text,symbol='*'):
	print '%s%s%s'%(symbol*10,text,symbol*10)

def greeting():
	post_fb_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%(PAGE_ACCESS_TOKEN)
	response_msg = {
			  "setting_type":"greeting",
			  "greeting":{
			    "text":"Hi! Welcome to this bot."
			  }
			}
	response_msg = json.dumps(response_msg)
	status = requests.post(post_fb_url,headers={"Content-Type": "application/json"},data=response_msg)
	logg(status.json(),'GR-1')

	response_obj = {
			  "setting_type":"call_to_actions",
			  "thread_state":"new_thread",
			  "call_to_actions":[
			    {
			      "payload":"Get Started"
			    }
			  ]
			}
	response_obj = json.dumps(response_obj)
	status = requests.post(post_fb_url,headers={"Content-Type": "application/json"},data=response_obj)
	logg(status.json(),'GR-2')

def domain_whitelist(domain='https://hackiitd.herokuapp.com'):
	post_message_url = "https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s"%(PAGE_ACCESS_TOKEN)
	response_object =	{
				"setting_type" : "domain_whitelisting",
				"whitelisted_domains" : [domain],
				"domain_action_type": "add"
			}
	response_msg = json.dumps(response_object)
	status = requests.post(post_message_url,headers={"Content-Type": "application/json"},data=response_msg)
	logg(status.json(),'-WHT-')

def set_menu():
	post_fb_url = 'https://graph.facebook.com/v2.6/me/thread_settings?access_token=%s'%(PAGE_ACCESS_TOKEN)
	response_msg = {
			"setting_type" : "call_to_actions",
			  "thread_state" : "existing_thread",
			  "call_to_actions":[
			    {
			      "type":"postback",
			      "title":"Contact Us",
			      "payload":"contact us"
			    },
			    {
			      "type":"postback",
			      "title":"Team",
			      "payload":"team"
			    },
			    {
			      "type":"web_url",
			      "title":"Login",
			      "url":"https://hackiitd.herokuapp.com/account",
			      "webview_height_ratio": "compact",
			      "messenger_extensions": True,
			    },
			    {
			      "type":"web_url",
			      "title":"View Website",
			      "url":"https://hackiitd.herokuapp.com"
			    }
			  ]
	}
	response_msg = json.dumps(response_msg)
	status = requests.post(post_fb_url,headers={"Content-Type": "application/json"},data=response_msg)
	logg(status.json(),'set-menu ')

def handle_quickreply(fbid, payload):
	pass

def handle_postback(fbid,payload):
	post_fb_url='https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	if payload=='Get Started':
		message = 'Welcome to alpha coders! What are you looking for?'
		response_qr = {
					"recipient":{
					    "id":fbid
					  },
					  "message":{
					    "text":message,
					    "quick_replies":[
					      {
					        "content_type":"text",
					        "title":"Question Arena",
					        "payload":"qarena"
					      },
					      {
					        "content_type":"text",
					        "title":"Upcoming Contests",
					        "payload":"upcontest"
					      },
					      {
					        "content_type":"text",
					        "title":"Rankings",
					        "payload":"upcontest"
					      }
					    ]
					  }
		}
		response_qr = json.dumps(response_qr)
		status = requests.post(post_fb_url, headers={"Content-Type": "application/json"},data=response_qr)
		logg(status.json(),'-QR-')
	else:
		pass

def post_fb_msg(fbid,message):
	post_fb_url='https://graph.facebook.com/v2.6/me/messages?access_token=%s'%PAGE_ACCESS_TOKEN
	response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text": message }})
	status = requests.post(post_fb_url, headers={"Content-Type": "application/json"},data=response_msg)
	logg(status.json(),'FB-MSG ')

class MyChatBotView(generic.View):
	def get(self,request,*args,**kwargs):
		if self.request.GET['hub.verify_token']==VERIFY_TOKEN:
			return HttpResponse(self.request.GET['hub.challenge'])
		else:
			return HttpResponse('oops invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self,request,*args,**kwargs):
		return generic.View.dispatch(self,request,*args,**kwargs)

	def post(self,request,*args,**kwargs):
		incoming_message=json.loads(self.request.body.decode('utf-8'))
		logg(incoming_message)
		for entry in incoming_message['entry']:
			for message in entry['messaging']:
				logg(message)
				try:
					if 'postback' in message:
						handle_postback(message['sender']['id'],message['postback']['payload'])
						return HttpResponse()
					else:
						pass
				except Exception as e:
					logg(e,symbol='-postback-')

				try:
					if 'quick_reply' in message['message']:
						handle_quickreply(message['sender']['id'],message['message']['quick_reply']['payload'])
						return HttpResponse()
					else:
						pass
				except Exception as e:
					logg(e,symbol='-quick_reply-')

				try:
					sender_id = message['sender']['id']
					message_text = message['message']['text']
					post_fb_msg(sender_id,message_text)
				
				except Exception as e:
					logg(e,symbol='-post_fb_msg-')

		return HttpResponse()
