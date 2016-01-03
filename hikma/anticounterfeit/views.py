# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Product, State, City, Pharmacy, Doctor, UniqueRandomNumbersGroup
from .akelsaman.Validator import Validator, ValidatorsArray
from .akelsaman.DjangoORM import DjangoORM
from .akelsaman.DateTimeObject import DateTimeObject


# Create your views here.
@ensure_csrf_cookie  # to force setting of csrf cookie if form added dynamically to the page - for example through jquery
def index(request):
	response = "AntiCounterFeit Home Page"
	return HttpResponse(response)


def check(request, QRCode=0):
	# c = {}
	# c.update(csrf(request))
	# return render_to_response('anticounterfeit/check.html', c)
	return render(request, 'anticounterfeit/check.html', {'QRCode': QRCode})


def addUniqueRandomNumbers(request):
	fieldName = ""
	if request.POST:
		# return render(request, 'anticounterfeit/UniqueRandomNumbers/addResult.html', {'postArray':request.POST})
		va = ValidatorsArray(request.POST, UniqueRandomNumbersGroup)
		vaHTML = va.runHTML()
		if vaHTML:
			return HttpResponse(vaHTML)
		else:
			#return HttpResponse("Else is work")
			#dict1 = UniqueRandomNumbersGroup.validatorsInputsDictionary()s
			fieldsDictionary = UniqueRandomNumbersGroup._meta.get_fields()
			#dict3 = UniqueRandomNumbersGroup.__base__.__name__
			#dict4 = UniqueRandomNumbersGroup.__name__

			#dorm = DjangoORM(UniqueRandomNumbersGroup)
			#dorm.insert(request.POST)

			for fieldKey in range (2, fieldsDictionary.__len__()):
				fieldName = fieldName + fieldsDictionary[fieldKey].name + "<br>"

			productInstance = Product.objects.get(id=request.POST["product"])
			urn = UniqueRandomNumbersGroup()
			urn.product = productInstance
			urn.internalOrExternal = request.POST["internalOrExternal"]
			urn.uniqueRandomNumbersCount = request.POST["uniqueRandomNumbersCount"]
			urn.batchNumber = request.POST["batchNumber"]

			dt = DateTimeObject()
			urn.dateAndTime = dt.getDateTimeObject(request.POST["dateAndTime"])
			urn.active = False
			try:
				urn.save()
			except Exception as e:
				result = str(e)

			if (urn.pk):
				result = "Has been saved successfully, ID# " + str(urn.pk)

			response = fieldName + "<br>" + result

			return HttpResponse(response)
	else:
		return render(request, 'anticounterfeit/UniqueRandomNumbers/add.html', )


def product(request):
	products = Product.objects.all()
	return render(request, 'anticounterfeit/product', {'products': products})


def state(request):
	states = State.objects.all()
	return render(request, 'anticounterfeit/state', {'states': states})


def city(request, stateID):
	cities = City.objects.filter(state=stateID)
	return render(request, 'anticounterfeit/city', {'cities': cities})


def pharmacy(request, cityID):
	pharmacies = Pharmacy.objects.filter(city=cityID)
	return render(request, 'anticounterfeit/pharmacy', {'pharmacies': pharmacies})


def doctor(request, cityID):
	doctors = Doctor.objects.filter(city=cityID)
	return render(request, 'anticounterfeit/doctor', {'doctors': doctors})


'''
def checkVariableValidator(request, variableValidator, regexPattern, errorMessage):
    import re
    if (re.match(regexPattern, variableValidator)):
        return HttpResponse(errorMessage)
'''


@ensure_csrf_cookie  # to force setting of csrf cookie if form added dynamically to the page - for example through jquery
def result(request):
	product = request.POST['product']
	productCode = request.POST['productCode']
	# pharmacy        = request.POST['pharmacy']
	# doctor          = request.POST['doctor']
	checker = request.POST['checker']
	# cheakerName     = request.POST['checkerName']
	'''
	productVariableValidator         = VariableValidator(product, r'\W|^$', u'Error:* من فضلك تأكد من إختيار المنتج')
	productCodeVariableValidator     = VariableValidator(productCode, r'\D|^$', u'Error:* من فضلك تأكد من ادخال كود المنتج بطريقة صحيح')
	checkerVariableValidator         = VariableValidator(checker, r'^أ-ى|^$', u'Error:* من فضلك تاكد من إدخال إسمك بطريقة صحيحة')

	arrayValidator = ArrayValidator([productVariableValidator, productCodeVariableValidator, checkerVariableValidator])
	if (arrayValidator.message() != ''):
		return HttpResponse(arrayValidator.message())
	'''
	product = Product.objects.get(id=product)
	# pharmacy        = Pharmacy.objects.get(id=pharmacy)
	# doctor          = Doctor.objects.get(id=doctor)

	postArray = {'product': product,
	             'pharmacy': pharmacy,
	             'doctor': doctor
	             }
	# c = {'product': product}
	# c.update(csrf(request))
	# return render_to_response('anticounterfeit/result.html', c)
	return render(request, 'anticounterfeit/result.html', postArray)
