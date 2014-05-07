from django.conf.urls import patterns, include, url
#from django.contrib import admin
#admin.autodiscover()
import os
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iwas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', home),
    url(r'^share/$', toshare),
    url(r'^about/$', about),
    url(r'^feedback/$', feedback),
    url(r'^thanks/$',thanks,name="thanks_page"),
    url(r'^feedback_thanks/$', feedback_thanks),
    #url(r'^admin/', include(admin.site.urls)),
)

