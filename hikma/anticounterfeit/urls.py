from django.conf.urls import url

from . import views

urlpatterns = [
               # ex: /anticounterfeit/
               url(r'^$', views.index, name='index'),
               # ex: /anticounterfeit/check/
               # ex: /anticounterfeit/check/5463192
               url(r'^(check/|check/(?P<QRCode>[0-9a-zA-Z]+))$', views.check, name='check'),
               # ex: /anticounterfeit/urn/add
               url(r'^urn$', views.uniqueRandomNumbers, name='uniqueRandomNumbers'),
               # ex: /anticounterfeit/urn/add
               url(r'^urn/add/$', views.uniqueRandomNumbersAdd, name='uniqueRandomNumbersAdd'),
               # ex: /anticounterfeit/urn/edit
               url(r'^urn/edit/$', views.uniqueRandomNumbersEdit, name='uniqueRandomNumbersEdit'),
               # ex: /anticounterfeit/urn/filters
               url(r'^urn/filters/$', views.uniqueRandomNumbersFilters, name='uniqueRandomNumbersFilters'),
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