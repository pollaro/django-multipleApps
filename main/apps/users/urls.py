from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^register/',views.newUser),
    url(r'^login/',views.login),
    url(r'^$',views.users),
    url(r'^new/',views.newUser)
]
