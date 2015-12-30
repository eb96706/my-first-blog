from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_lits'), # so only empty string will match 
	'''
	http://127.0.0.1:8000/ is not part of the URL, this pattern will tell django that
	views.post_list is the right place to go if someone enters your website at the 
	http://127.0.0.1:8000/' address

	the last part name='post_list' is the name of the url that will be used to identify the views

	no attribute 'post_list' this everything is in place but we just haven't created our view yet.
	
	'''
]