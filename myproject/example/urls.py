from django.conf.urls import url

from example import views

urlpatterns = [
    url(r'hello/',views.hello),
    url(r'temp/',views.hello_temp)
]