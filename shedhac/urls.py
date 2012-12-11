from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('main.views',
    (r'^$', 'app_index'),
)

urlpatterns += patterns('control.views',
    url(r'^control/$', 'index'),
    url(r'^control/lights/$', 'index'),
    url(r'^control/light/(?P<light_id>\d+)/$', 'light'),
    #('^control/light/(\d+)/$', 'light'),
    url(r'^control/light/(?P<light_id>\d+)/on/$', 'lighton'),
    url(r'^control/light/(?P<light_id>\d+)/off/$', 'lightoff'),
    url(r'^control/light/(?P<light_id>\d+)/history/$', 'lighthistory'),
    url(r'^control/lights/button/(?P<btn_id>\d{2})/$', 'button'),
    url(r'^control/lights/all/on/$', 'allon'),
    url(r'^control/lights/all/off/$', 'alloff'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^login/$','django.contrib.auth.views.login',
        #dict(
        #    template_name = 'jqm/login.html',
        #),
        name='login',
    ),
    url(
        r'^logout/$','django.contrib.auth.views.logout',
        #dict(
        #    template_name = 'jqm/logout.html',
        #),
        name='logout',
    ),
)