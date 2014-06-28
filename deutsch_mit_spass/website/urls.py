from django.conf.urls import patterns, url

urlpatterns = patterns(
    'website.views',
    url(r'^$', 'welcome', name='index'),
    url(r'^login$', 'login_view', name='login'),
    url(r'^welcome$', 'welcome', name='welcome'),
    url(r'^logout$', 'logout_view', name='logout'),
    url(r'^register$', 'register_view', name='register'),
    url(r'^exercises$', 'exercises_view', name='exercises'),
    url(r'^correction$', 'correction_view', name='correction'),
    url(r'^translation$', 'translation_view', name='translation'),
    url(r'^reading$', 'reading_view', name='reading'),
    url(r'^fillin$', 'fill_in_view', name='fillin'),
    url(r'^ordering$', 'ordering_view', name='ordering'),
    url(r'^doexercises$', 'do_exercises', name='doexercises'),
    url(r'^docorrections$', 'do_correcting_exercises', name='docorrections'),
    url(r'^dotranslations$', 'do_translating_exercises',
        name='dotranslations'),
    url(r'^doreading$', 'do_reading_exercises', name='dotranslations'),
    url(r'^dofillins$', 'do_fill_in_exercises', name='dofillins'),
    url(r'^doorderings$', 'do_ordering_exercises', name='doordering')
)
