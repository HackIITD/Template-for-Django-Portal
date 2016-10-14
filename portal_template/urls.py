from django.conf.urls import patterns, include, url
from django.contrib import admin
from chatbot.views import MyChatBotView, index as indexbot

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal_template.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',"webportal.views.index",name="homepage"),
    url(r'^account$',"webportal.views.account",name="account"),
    url(r'^facebook_auth/?$', MyChatBotView.as_view(), name='fb_callback'),
    url(r'^chatbot/?$', indexbot, name='indexbot'),
)
