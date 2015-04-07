from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dip.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^clients/', include('oper.urls')),
    #url(r'^operators/', include('oper.urls')),
    url(r'^auth/', include('singin.urls')),
    #url(r'^index/', include('singin.urls')),
    url(r'^', include('oper.urls')),

)
