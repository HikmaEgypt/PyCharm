# -*- coding: utf-8 -*-

# how to:
#   ake = Validator(ANYVARIABLE, "Empty,Dshs,Spcs")
#   print(ake.run())
#   va = ValidatorsArray(DICTIONARY[Ex. request.POST], MODELNAME[Ex. UniqueRandomNumbersGroup])
#   print(va.runHTML())

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
	def __init__(self, validatorsInputs, modelClass):
		self.validatorsInputs = validatorsInputs
		self.modelObject = modelClass()
		self.modelObjectFieldsNames = self.modelObject._meta.get_fields()
		self.fieldsValidatorsRulesDictionary = self.modelObject.fieldsValidatorsRulesDictionary()
		self.validatorsArrayMessage = ""

	def runText(self):
		self.run()
		if self.validatorsArrayMessage:
			self.textMessage()
		return self.validatorsArrayMessage

	def runHTML(self):
		self.run()
		if self.validatorsArrayMessage:
			self.htmlMessage()
		return self.validatorsArrayMessage

	def run(self):
		self.validatorsArrayMessage = ""
		for key in range (1, self.modelObjectFieldsNames.__len__()):
			fieldName = self.modelObjectFieldsNames[key].name
			try:
				validatorRules = self.fieldsValidatorsRulesDictionary[fieldName]
				try:
					validatorInput = self.validatorsInputs[fieldName]
					validator = Validator(validatorInput,validatorRules)
					validatorMessage = validator.run()
				except KeyError:
					validatorInput = ""
					validatorMessage = "{{MessageLine::Missing input::MessageLine}}"
				if(validatorMessage):
					validatorMessage = "{{h1:: * Input\t: " + fieldName + "::h1}}\n" + \
					                   "{{h2:: * Value\t: " + validatorInput + "::h2}}\n" + \
					                   validatorMessage
					self.validatorsArrayMessage = self.validatorsArrayMessage + "\n\n" + validatorMessage
			except KeyError:
				pass

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