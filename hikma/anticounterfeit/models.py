import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
    product         = models.CharField('Product', null=False, blank=False, unique=True, max_length=20)
    image           = models.ImageField(upload_to='%y%m%d', height_field=None, width_field=None, max_length=100)
    
    def image_thumb(self):
        return '<img src="/media/%s" width="100" height="100" />' % (self.image)
    
    image_thumb.short_description = 'Image'
    image_thumb.allow_tags = True
    
    def __unicode__(self):
        return self.product

class publicCode(models.Model):
    publicCode      = models.BigIntegerField('Public Code', null=False, blank=False, unique=True)
    active          = models.BooleanField('Active', default=False, null=False, blank=False)
    product         = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
    
    def __unicode__(self):
        return self.publicCode

class UserCode(models.Model):
    userCode        = models.BigIntegerField('User Code', null=False, blank=False, unique=True)
    active          = models.BooleanField('Active', default=False, null=False, blank=False)
    product         = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
    
    def __unicode__(self):
        return self.userCode

class State (models.Model):
    state           = models.CharField('State', null=False, blank=False, unique=True, max_length=20)

    def __unicode__(self):
        return self.state
    
class City(models.Model):
    city            = models.CharField('City', null=False, blank=False, unique=True, max_length=20)
    state           = models.ForeignKey(State, null=False, blank=False, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.city
    
    class Meta:
        unique_together=(("city", "state"),)
    
class Pharmacy(models.Model):
    pharmacy        = models.CharField('Pharmacy', null=False, blank=False, unique=True, max_length=50)
    city            = models.ForeignKey(City, null=False, blank=False, on_delete=models.PROTECT)
    
    def __unicode__(self):
        return self.pharmacy
    
    def state(self):
        return self.city.state
    
    class Meta:
        unique_together=(("pharmacy", "city"),)
        
class Doctor(models.Model):
    doctor          = models.CharField('Doctor', null=False, blank=False, unique=True, max_length=50)
    city            = models.ForeignKey(City, null=False, blank=False, on_delete=models.PROTECT)
    
    def __unicode__(self):
        return self.doctor
    
    def state(self):
        return self.city.state
    
    class Meta:
        unique_together=(("doctor", "city"),)

class Check(models.Model):
    productFK       = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
    pharmacyFK      = models.ForeignKey(Pharmacy, null=False, blank=False, on_delete=models.PROTECT)
    doctorFK        = models.ForeignKey(Doctor, null=False, blank=False, on_delete=models.PROTECT)
    checker         = models.CharField('Checker', null=False, blank=False, max_length=50)
    checkerMobile   = models.CharField('Cheaker Mobile', null=False, blank=False, max_length=11)
    checkerEmail    = models.CharField('Cheaker Email', null=False, blank=False, max_length=50)