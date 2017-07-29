from django.conf.urls import url
from django.contrib import auth
from django.contrib.auth import views as auth_views
from . import views as vapp_views

urlpatterns = [
	url(r'^$', vapp_views.home, name='home'),
	url(r'^delete/(?P<pk>\d+)/$', vapp_views.home, name='delete_item'),
	url(r'^vote/$', vapp_views.vote_item, name='vote_item'),

	url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}),
	url(r'^logout/$', auth_views.logout,name="logout"),
	url(r'^pchange/$', auth_views.password_change, {'post_change_redirect':'/'},name='password_change'),
]