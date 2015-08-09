from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^admin/$', include(admin.site.urls)),
                       url(r'^$', 'pagina.views.home', name='home'),
                       url(r'^broma/$', 'pagina.views.broma', name='broma'),
                       url(r'^proyectos/$', 'pagina.views.proyectos', name='proyectos'),
                       url(r'^curriculum/$', 'pagina.views.curriculum', name='curriculum'),
                       url(r'^cronometro/$', 'pagina.views.cronometro', name='cronometro'),
                       url(r'^conversor/$', 'pagina.views.conversor', name='conversor'),
                       url(r'^contacto/$', 'pagina.views.contacto', name='contacto'),
                       url(r'^calculadora/$', 'pagina.views.calculadora', name='calculadora'),
                       url(r'^ver_post/(?P<id_post>[0-9]+)/$', 'pagina.views.ver_post', name='vermipost'),
                       url(r"^enviar_comentarios/$", 'pagina.views.enviar_comentarios', name='enviar_comentarios'),
                      )