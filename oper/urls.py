from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dip.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^clients/all/$', 'oper.views.clients'),
    url(r'^operators/all/$', 'oper.views.operators'),
    url(r'^clients/get/(?P<client_id>\d+)/$', 'oper.views.client'),
    url(r'^operators/get/(?P<operator_id>\d+)/$', 'oper.views.operator'),
    url(r'^tariff/$', 'oper.views.tariff'),
    url(r'^$', 'oper.views.enter'),
)

