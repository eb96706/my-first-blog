from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #for URL that starts with admin/ Django will find corresponding view
    url(r'', include('blog.urls')), #Django will now redirect everything that comes into http://localhost:8000 and look for further instruction
    # r in front of the string helps Python to expect may contain special characters
]
