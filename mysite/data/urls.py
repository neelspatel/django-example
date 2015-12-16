from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('',	
	#the ^ character indicates the start of the regex, and the $ indicates the end
	#this line defines a blank URL, which will direct to home
	url(r'^$', 'data.views.test', name='test'),		

	#however, if instead of a blank URL, we pass a specific value, we can act on that
	url(r'^other/$', 'data.views.other', name='other'),		

	#we can even pass a variable in to the url
	url(r'^parameter/(?P<value>\w+)$', 'data.views.parameter', name='parameter'),	

	url(r'^home/$', 'data.views.home', name='home'),		
	url(r'^get_data/$', 'data.views.get_data', name='get_data'),	
)

