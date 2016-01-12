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

class Validator:
	def __init__(self, validatorInput, validatorRules):
		self.validatorInput = validatorInput
		self.validatorRules = validatorRules.split(",")
		self.validatorsRulesLength = self.validatorRules.__len__()
		self.validatorMessage = ""

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

class ValidatorsArray:
	def __init__(self, validatorsInputs, fieldsValidatorsRulesDictionary):
		self.validatorsInputs = validatorsInputs
		self.fieldsValidatorsRulesDictionary = fieldsValidatorsRulesDictionary
		self.validatorsArrayMessage = ""

	def runAndReturnValidatorArrayMessageInFormat(self, validatorArrayMessageFormat):
		self.run()
		if self.validatorsArrayMessage:
			if validatorArrayMessageFormat=="text": self.textMessage()
			if validatorArrayMessageFormat=="html": self.htmlMessage()
		return self.validatorsArrayMessage

	def run(self):
		self.validatorsArrayMessage = ""
		for fieldName in self.fieldsValidatorsRulesDictionary:
			if self.fieldsValidatorsRulesDictionary[fieldName] is not "":
				validatorRules = self.fieldsValidatorsRulesDictionary[fieldName]
				try:
					validatorInput = self.validatorsInputs[fieldName]
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
					self.validatorsArrayMessage = self.validatorsArrayMessage + "\n\n" + validatorMessage

	def textMessage(self):
		self.validatorsArrayMessage = re.sub('{{h1::', '', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('::h1}}', '', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('{{h2::', '', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('::h2}}', '', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('{{MessageLine::', '\t>', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('::MessageLine}}', '', self.validatorsArrayMessage)

	def htmlMessage(self):
		self.validatorsArrayMessage = re.sub('{{h1::', '\t<tr><th>', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('::h1}}', '</th></tr>', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('{{h2::', '\t<tr><th>', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('::h2}}', '</th></tr>', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('{{MessageLine::', '\t<tr><td>', self.validatorsArrayMessage)
		self.validatorsArrayMessage = re.sub('::MessageLine}}', '</td></tr>', self.validatorsArrayMessage)
		self.validatorsArrayMessage = "<table class='validationTable'><thead></thead><tfoot></tfoot><tbody>" \
		                              + self.validatorsArrayMessage \
		                              + "\n\n</tbody></table>"

		self.validatorsArrayMessage = '''Error:
		<html>
			<head>
				<title>Add Unique Random Numbers Validator</title>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<LINK REL=StyleSheet HREF="/static/UniqueRandomNumbers/add.css" TYPE="text/css">
			</head>
			<body>
		''' + self.validatorsArrayMessage + '''
			</body>
		</html>'''