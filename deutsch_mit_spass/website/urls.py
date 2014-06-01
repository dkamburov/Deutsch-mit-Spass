from django.conf.urls import patterns, url

urlpatterns = patterns('website.views',
    url(r'^$', 'welcome', name='index'),
    url(r'^login$', 'login_view', name='login'),
    url(r'^welcome$', 'welcome', name='welcome'),
    url(r'^logout$', 'logout_view', name='logout'),
    url(r'^register$', 'register_view', name='register'),
    url(r'^exercises$', 'exercises_view', name='exercises'),
    url(r'^correction$', 'correction_view', name='correction')
)
