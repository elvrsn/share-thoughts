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
    url(r'^shared/$', shared),
    url(r'^thanks$',thanks),
    #url(r'^admin/', include(admin.site.urls)),
)


#from django.conf import settings
#from django.conf.urls.static import static
#
#urlpatterns += patterns('',
#    # ... the rest of your URLconf goes here ...
#) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#
#
#if settings.DEBUG:
#    urlpatterns += patterns('',
#        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.realpath(__file__)),'static')}),
#    )
