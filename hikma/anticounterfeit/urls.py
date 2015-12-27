from django.conf.urls import url

from . import views

urlpatterns = [
               # ex: /anticounterfeit/
               url(r'^$', views.index, name='index'),
               # ex: /anticounterfeit/check/
               # ex: /anticounterfeit/check/5463192
               url(r'^(check/|check/(?P<QRCode>[0-9a-zA-Z]+))$', views.check, name='check'),
               # ex: /anticounterfeit/UniqueRandomNumbers/add
               url(r'^UniqueRandomNumbers/add/$', views.addUniqueRandomNumbers, name='addUniqueRandomNumbers'),
               # ex: /anticounterfeit/product/
               url(r'^product/$', views.product, name='product'),
               # ex: /anticounterfeit/state
               url(r'^state/$', views.state, name='state'),
               # ex: /anticounterfeit/04/city
               url(r'^(?P<stateID>[0-9]+)/city$', views.city, name='city'),
               # ex: /anticounterfeit/01/pharmacy
               url(r'^(?P<cityID>[0-9]+)/pharmacy$', views.pharmacy, name='pharmacy'),
               # ex: /anticounterfeit/01/doctor
               url(r'^(?P<cityID>[0-9]+)/doctor$', views.doctor, name='doctor'),
               # ex: /anticounterfeit/result
               url(r'^result/$', views.result, name='result'),
]