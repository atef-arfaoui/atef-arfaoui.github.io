from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'test1.views.index'),
    #user auth urls
    url(r'^accounts/login/$', 'test1.views.login'),
    url(r'^accounts/auth/$', 'test1.views.auth_view'),
    url(r'^accounts/logout/$', 'test1.views.logout'),
    url(r'^accounts/loggedin/$', 'test1.views.loggedin'),
    url(r'^accounts/invalid/$', 'test1.views.invalid_login'),
    url(r'^accounts/register/$', 'test1.views.register_user'),
    url(r'^accounts/register_success/$', 'test1.views.register_success'),

)
