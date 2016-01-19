# -*- coding: utf-8 -*-

from django.db import models
from .akelsaman.DateTimeObject import DateTimeObject
from collections import OrderedDict
from django.utils import timezone


# Create your models here.
# ============================================================================ #
class Product(models.Model):
	product = models.CharField('Product', null=False, blank=False, unique=True, max_length=20)
	image = models.ImageField(upload_to='%y%m%d', height_field=None, width_field=None, max_length=100)

	def image_thumb(self):
		return '<img src="/media/%s" width="100" height="100"/>' % (self.image)

	image_thumb.short_description = 'Image'
	image_thumb.allow_tags = True

	def __unicode__(self):
		return self.product
# ============================================================================ #
class UniqueRandomNumbers(models.Model):
	product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
	internalOrExternal = models.CharField('Internal Or External', null=False, blank=False, max_length=8)
	count = models.PositiveIntegerField('count', null=False, blank=False)
	batchNumber = models.PositiveSmallIntegerField('Batch Number', null=False, blank=False)
	dateAndTime = models.DateTimeField('Date and Time', null=False, blank=False, unique=True)
	active = models.BooleanField('Active', default=False, null=False, blank=False)

	def __unicode__(self):
		#TypeError: coercing to Unicode: need string or buffer, int found
		return str(self.id)

	def fieldsValidatorsRulesDictionary(self):
		fieldsValidatorsRulesDictionary = OrderedDict()
		fieldsValidatorsRulesDictionary["id"] = ""
		fieldsValidatorsRulesDictionary["product"] = "Empty,Dg"
		fieldsValidatorsRulesDictionary["internalOrExternal"] = "Empty,internalOrExternal"
		fieldsValidatorsRulesDictionary["count"] = "Empty,Dg"
		fieldsValidatorsRulesDictionary["batchNumber"] = "Empty,EnSmCpDg"
		fieldsValidatorsRulesDictionary["dateAndTime"] = "Empty,Month01-12,MonthFormatIsWrong,Day01-31,DayFormatIsWrong,Hour00-23,HourFormatIsWrong,Minute00-59,MinuteFormatIsWrong,YYYY.MM.DD HH:MM"
		fieldsValidatorsRulesDictionary["active"] = ""

		return fieldsValidatorsRulesDictionary

	def searchSelectSQL(self):
		searchSelectSQL = '''
			SELECT anticounterfeit_UniqueRandomNumbers.id,
			anticounterfeit_UniqueRandomNumbers.product_id,
			anticounterfeit_UniqueRandomNumbers.internalOrExternal,
			anticounterfeit_UniqueRandomNumbers.count,
			anticounterfeit_UniqueRandomNumbers.batchNumber,
			anticounterfeit_UniqueRandomNumbers.dateAndTime,
			anticounterfeit_UniqueRandomNumbers.active
			FROM anticounterfeit_UniqueRandomNumbers INNER JOIN  anticounterfeit_Product
			ON anticounterfeit_UniqueRandomNumbers.product_id = anticounterfeit_Product.id
			WHERE
			'''
		return searchSelectSQL

	def insert(self, inputs):
		productInstance = Product.objects.get(id=inputs["product"])
		self.product = productInstance
		self.internalOrExternal = inputs["internalOrExternal"]
		self.count = inputs["count"]
		self.batchNumber = inputs["batchNumber"]

		dt = DateTimeObject()
		self.dateAndTime = dt.getDateTimeObject(inputs["dateAndTime"])
		self.active = False
		try:
			self.save()
			if self.pk:
				result = str(self.pk)
		except Exception as e:
			result = str(e)

		return result

	def select(self):
		outputs = OrderedDict()
		outputs["id"] = self.id
		outputs["product"] = self.product.product
		outputs["internalOrExternal"] = self.internalOrExternal
		outputs["count"] = self.count
		outputs["batchNumber"] = self.batchNumber
		outputs["dataAndTime"] = self.dateAndTime
		return outputs

	def getHTMLRow(self, htmlTable):
		outputs = self.select()
		tdList = []
		for key in outputs:
			tdList.append(outputs[key])
		htmlTable.getRow(tdList)
		return htmlTable
# ============================================================================ #
class UniqueRandomNumber(models.Model):
	uniqueRandomNumber = models.CharField('Unique Random Number', null=False, blank=False, unique=True, max_length=12)
	uniqueRandomNumbers = models.ForeignKey(UniqueRandomNumbers, null=False, blank=False,
	                                             on_delete=models.PROTECT)

	def __unicode__(self):
		return self.uniqueRandomNumber
# ============================================================================ #
class State(models.Model):
	state = models.CharField('State', null=False, blank=False, unique=True, max_length=20)

	def __unicode__(self):
		return self.state
# ============================================================================ #
class City(models.Model):
	city = models.CharField('City', null=False, blank=False, unique=True, max_length=20)
	state = models.ForeignKey(State, null=False, blank=False, on_delete=models.PROTECT)

	def __unicode__(self):
		return self.city

	class Meta:
		unique_together = (("city", "state"),)
# ============================================================================ #
class Pharmacy(models.Model):
	pharmacy = models.CharField('Pharmacy', null=False, blank=False, unique=True, max_length=50)
	city = models.ForeignKey(City, null=False, blank=False, on_delete=models.PROTECT)

	def __unicode__(self):
		return self.pharmacy

	def state(self):
		return self.city.state.state

	class Meta:
		unique_together = (("pharmacy", "city"),)

	def select(self):
		outputs = OrderedDict()
		outputs["id"] = self.id
		outputs["pharmacy"] = self.pharmacy
		outputs["city"] = self.city.city
		outputs["state"] = self.state()
		return outputs

	def getHTMLRow(self, htmlTable):
		outputs = self.select()
		tdList = []
		for key in outputs:
			tdList.append(outputs[key])
		htmlTable.getRow(tdList)
		return htmlTable
# ============================================================================ #
class Doctor(models.Model):
	doctor = models.CharField('Doctor', null=False, blank=False, unique=True, max_length=50)
	city = models.ForeignKey(City, null=False, blank=False, on_delete=models.PROTECT)

	def __unicode__(self):
		return self.doctor

	def state(self):
		return self.city.state

	class Meta:
		unique_together = (("doctor", "city"),)
# ============================================================================ #
class Check(models.Model):
	productFK = models.ForeignKey(Product, null=False, blank=False, on_delete=models.PROTECT)
	pharmacyCityFK = models.ForeignKey(Pharmacy, null=False, blank=False, on_delete=models.PROTECT)
	doctorCityFK = models.ForeignKey(Doctor, null=False, blank=False, on_delete=models.PROTECT)
	checker = models.CharField('Checker', null=False, blank=False, max_length=50)
	checkerMobile = models.CharField('Cheaker Mobile', null=False, blank=False, max_length=11)
	checkerEmail = models.CharField('Cheaker Email', null=False, blank=False, max_length=50)
# ============================================================================ #
'''
	SELECT *
	FROM TABLENAME
	INNER JOIN
	anticounterfeit_Product,
	anticounterfeit_UniqueRandomNumbers,
	anticounterfeit_UniqueRandomNumber,
	anticounterfeit_City,
	anticounterfeit_State,
	anticounterfeit_Pharmacy,
	anticounterfeit_Doctor
	ON
	anticounterfeit_UniqueRandomNumbers.product_id = anticounterfeit_Product.id
	AND anticounterfeit_UniqueRandomNumber.uniqueRandomNumbers_id = anticounterfeit_UniqueRandomNumber.id
	AND anticounterfeit_Pharmacy.city_id = anticounterfeit_City.id
	AND anticounterfeit_Doctor.city_id = anticounterfeit_City.id
	AND anticounterfeit_City.state_id = anticounterfeit_State.id
'''
'''
	SELECT anticounterfeit_Pharmacy.id
	FROM anticounterfeit_Pharmacy
	INNER JOIN
	anticounterfeit_City,
	anticounterfeit_State
	ON
	anticounterfeit_Pharmacy.city_id = anticounterfeit_City.id
	AND anticounterfeit_City.state_id = anticounterfeit_State.id
	WHERE anticounterfeit_State.id=2
'''