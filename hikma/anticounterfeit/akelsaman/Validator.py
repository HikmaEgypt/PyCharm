# -*- coding: utf-8 -*-

# how to:
#   ake = Validator(ANYVARIABLE, "Empty,Dshs,Spcs")
#   print(ake.run())
#   va = ValidatorsArray(DICTIONARY[Ex. request.POST], MODELNAME[Ex. UniqueRandomNumbersGroup])
#   print(va.runHTML())

# Tips:
#   UniqueRandomNumbersGroup.__name__ # UniqueRandomNumbersGroup.__base__.__name__
#   self.modelObjectFieldsNames = self.modelObject._meta.get_fields()

import re
from .validatorSettings import validatorPatterns, validatorMessages
#==============================================================================#
class Validator:
	def __init__(self, validatorInput, validatorRules):
		self.validatorInput = validatorInput
		self.validatorRules = validatorRules.split(",")
		self.validatorsRulesLength = self.validatorRules.__len__()
		self.validatorMessage = ""
#------------------------------------------------------------------------------#
	def run(self):
		self.validatorMessage = ""
		for i in range(0, self.validatorsRulesLength - 1):
			validatorPattern = validatorPatterns[self.validatorRules[i]]
			validatorMessage = validatorMessages[self.validatorRules[i]]
			searchObject = re.search(validatorPattern, self.validatorInput)
			if (searchObject):
				validatorMessage = "{{MessageLine::" + validatorMessage + "::MessageLine}}"
				self.validatorMessage = self.validatorMessage + "\n" + validatorMessage

		# last rule is the rule of the accepted pattern

		validatorPattern = validatorPatterns[self.validatorRules[self.validatorsRulesLength - 1]]
		validatorMessage = validatorMessages[self.validatorRules[self.validatorsRulesLength - 1]]
		searchObject = re.search(validatorPattern, self.validatorInput)
		if not (searchObject):
			validatorMessage = "{{MessageLine::" + validatorMessage + "::MessageLine}}"
			self.validatorMessage = self.validatorMessage + "\n" + validatorMessage

		self.validatorMessage = re.sub('^\n', '', self.validatorMessage)
		return self.validatorMessage
# ============================================================================ #
class ValidatorsArray:
	def __init__(self):
		self.validatorsInputsDictionary = ""
		self.validatorsInputsArraysDictionay = ""
		self.fieldsValidatorsRulesDictionary = ""
		self.validatorsDictionaryMessage = ""
# ---------------------------------------------------------------------------- #
	def runDictionary(self, validatorsInputsDictionary, fieldsValidatorsRulesDictionary, validatorsDictionaryMessageFormat=""):
		self.validatorsInputsDictionary = validatorsInputsDictionary
		self.fieldsValidatorsRulesDictionary = fieldsValidatorsRulesDictionary
		self.validatorsDictionaryMessage = ""
		for fieldName in self.fieldsValidatorsRulesDictionary:
			if self.fieldsValidatorsRulesDictionary[fieldName] is not "":
				validatorRules = self.fieldsValidatorsRulesDictionary[fieldName]
				try:
					validatorInput = self.validatorsInputsDictionary[fieldName]
					validator = Validator(validatorInput,validatorRules)
					validatorMessage = validator.run()
				# if you are using MultiValueDictKeyError, from django.utils.datastructures import MultiValueDictKeyError
				except KeyError:
					validatorInput = ""
					validatorMessage = "{{MessageLine::Missing input::MessageLine}}"
				if(validatorMessage):
					validatorMessage = "{{h1:: * Input\t: " + fieldName + "::h1}}\n" + \
					                   "{{h2:: * Value\t: " + validatorInput + "::h2}}\n" + \
					                   validatorMessage
					self.validatorsDictionaryMessage = self.validatorsDictionaryMessage + "\n\n" + validatorMessage

		if validatorsDictionaryMessageFormat=="text": self.textMessage()
		if validatorsDictionaryMessageFormat=="html": self.htmlMessage()
		return self.validatorsDictionaryMessage
#------------------------------------------------------------------------------#
	def runArraysDictionary(self, validatorsInputsArraysDictionay, fieldsValidatorsRulesDictionary, validatorsDictionaryMessageFormat=""):
		self.validatorsInputsArraysDictionay = validatorsInputsArraysDictionay
		self.fieldsValidatorsRulesDictionary = fieldsValidatorsRulesDictionary
		self.validatorsDictionaryMessage = ""
		for fieldName in self.fieldsValidatorsRulesDictionary:
			if self.fieldsValidatorsRulesDictionary[fieldName] is not "":
				validatorRules = self.fieldsValidatorsRulesDictionary[fieldName]
				try:
					validatorInputsArray = self.validatorsInputsArraysDictionay[fieldName]
					for input in validatorInputsArray:
						validator = Validator(input,validatorRules)
						validatorMessage = validator.run()
						validatorMessage = "{{h2:: * Value\t: " + validatorInput + "::h2}}\n" + validatorMessage
				# if you are using MultiValueDictKeyError, from django.utils.datastructures import MultiValueDictKeyError
				except KeyError:
					validatorInput = ""
					validatorMessage = "{{MessageLine::Missing input::MessageLine}}"
				if(validatorMessage):
					validatorMessage = "{{h1:: * Input\t: " + fieldName + "::h1}}\n" + \
					                   validatorMessage
					self.validatorsDictionaryMessage = self.validatorsDictionaryMessage + "\n\n" + validatorMessage

		if validatorsDictionaryMessageFormat=="text": self.textMessage()
		if validatorsDictionaryMessageFormat=="html": self.htmlMessage()
		return self.validatorsDictionaryMessage
#------------------------------------------------------------------------------#
	def textMessage(self):
		self.validatorsDictionaryMessage = re.sub('{{h1::', '', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('::h1}}', '', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('{{h2::', '', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('::h2}}', '', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('{{MessageLine::', '\t>', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('::MessageLine}}', '', self.validatorsDictionaryMessage)
#------------------------------------------------------------------------------#
	def htmlMessage(self):
		self.validatorsDictionaryMessage = re.sub('{{h1::', '\t<tr><th>', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('::h1}}', '</th></tr>', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('{{h2::', '\t<tr><th>', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('::h2}}', '</th></tr>', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('{{MessageLine::', '\t<tr><td>', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = re.sub('::MessageLine}}', '</td></tr>', self.validatorsDictionaryMessage)
		self.validatorsDictionaryMessage = "<table class='validationTable'><thead></thead><tfoot></tfoot><tbody>" \
		                              + self.validatorsDictionaryMessage \
		                              + "\n\n</tbody></table>"

		self.validatorsDictionaryMessage = '''Error:
		<html>
			<head>
				<title>Add Unique Random Numbers Validator</title>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<LINK REL=StyleSheet HREF="/static/UniqueRandomNumbers/add.css" TYPE="text/css">
			</head>
			<body>
		''' + self.validatorsDictionaryMessage + '''
			</body>
		</html>'''