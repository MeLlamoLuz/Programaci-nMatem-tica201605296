from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^regex/$', view=ExpresionView, name='regex'),
    #url(r'^generado/$', view=AutomataView, name='autgen'),
]