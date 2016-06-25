from django.conf.urls import url

from . import views
# In our urlpatterns list we are calling a nice regex from beginning to end of views.index with the name variable being set to index.
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
