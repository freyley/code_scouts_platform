from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'code_scouts_platform.views.home', name='home'),
    # url(r'^code_scouts_platform/', include('code_scouts_platform.foo.urls')),
    ('^events/', include('events.urls'))
)

if settings.DEBUG:
    from django.contrib import admin

    admin.autodiscover()
    urlpatterns += patterns(
        '',
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
        url(r'^admin/', include(admin.site.urls)),
    )
