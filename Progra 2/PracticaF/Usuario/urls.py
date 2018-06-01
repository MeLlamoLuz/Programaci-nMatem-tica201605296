from django.conf.urls import url
from django.contrib.auth.views import LogoutView

from Usuario.views import RegistroUsuarioVista, LoginUsuarioVista, DashboardVista

urlpatterns = [
    # /account/register
    url(r'^registro/$', view=RegistroUsuarioVista.as_view(), name='registro'),
    url(r'^login/$', view=LoginUsuarioVista.as_view(), name='login'),
    url(r'^logout/$', view=LogoutView.as_view(), name='logout'),
    url(r'^dashboard/$', view=DashboardVista.as_view(), name='dashboard')
]