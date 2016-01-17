# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.template.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Product, State, City, Pharmacy, Doctor, UniqueRandomNumbers
from django.db.models import Q
from .akelsaman.Validator import Validator, ValidatorsDictionary
from .akelsaman.HTML import HTMLTable

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

def uniqueRandomNumbers(request):
	#uniqueRandomNumbers = UniqueRandomNumbers.objects.all()
	#uniqueRandomNumbers = UniqueRandomNumbers.objects.filter(Q(internalOrExternal__in=["Internal"]) & Q(batchNumber__in=[123, 789]))
	uniqueRandomNumbers = UniqueRandomNumbers.objects.filter(Q(id__lte=10))
	htmlTable = HTMLTable()
	for uniqueRandomNumber in uniqueRandomNumbers:
		htmlTable = uniqueRandomNumber.getHTMLRow(htmlTable)
	htmlTable = htmlTable.createTable("anyClass")
	return HttpResponse(htmlTable)

def uniqueRandomNumbersAdd(request):
	uniqueRandomNumbers = UniqueRandomNumbers()
	if request.POST:
		fieldsValidatorsRulesDictionary = uniqueRandomNumbers.fieldsValidatorsRulesDictionary()
		va = ValidatorsDictionary()
		vaHTML = va.run(request.POST, "Dictionary", fieldsValidatorsRulesDictionary, True, 'html')
		if vaHTML:
			return HttpResponse(vaHTML)
		else:
			response = uniqueRandomNumbers.insert(request.POST)
			return HttpResponse(response)
	else:
		return render(request, 'anticounterfeit/UniqueRandomNumbers/add.html', )

def uniqueRandomNumbersEdit(request, urn=0):
	pass

def uniqueRandomNumbersFilters(request):
	uniqueRandomNumbers = UniqueRandomNumbers()
	if request.POST:
		fieldsValidatorsRulesDictionary = uniqueRandomNumbers.fieldsValidatorsRulesDictionary()
		va = ValidatorsDictionary()
		vaHTML = va.run(request.POST, "ArraysDictionary", fieldsValidatorsRulesDictionary, False, 'html')
		if vaHTML:
			return HttpResponse(vaHTML)
		else:
			'''
			kwargs = {
			    '{0}__{1}'.format('name', 'startswith'): 'A',
			    '{0}__{1}'.format('name', 'endswith'): 'Z'
			}

			Person.objects.filter(**kwargs)
			'''
			cc = "Product001"
			bb = Q(product__product=cc)
			aa = Q(id__lte=10) & bb
			uniqueRandomNumbers = UniqueRandomNumbers.objects.filter(aa)
			htmlTable = HTMLTable()
			for uniqueRandomNumber in uniqueRandomNumbers:
				htmlTable = uniqueRandomNumber.getHTMLRow(htmlTable)
			htmlTable = htmlTable.createTable("anyClass")
			return HttpResponse(htmlTable)
	else:
		return render(request, 'anticounterfeit/UniqueRandomNumbers/filters.html', )

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
