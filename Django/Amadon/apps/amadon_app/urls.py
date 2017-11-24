from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^Amadon/buy/(?P<item_id>\d+)$', views.buy),
    url(r'^Amadon/checkout$', views.checkout),
    url(r'^reset$', views.reset)
]
