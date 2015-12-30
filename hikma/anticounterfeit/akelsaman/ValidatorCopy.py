# how to:
#   ake = Validator(ANYVARIABLE, "Empty,Dshs,Spcs")
#   print(ake.run())

import re
from django.utils.datastructures import MultiValueDictKeyError
from .validatorSettings import validatorPatterns, validatorMessages



class Validator:
	def __init__(self, validatorInput, validatorRules):
		self.validatorInput = validatorInput
		self.validatorRules = validatorRules.split(",")
		self.validatorsRulesLength = self.validatorRules.__len__()
		self.validatorMessage = ""

	def run(self):
		for i in range(0, self.validatorsRulesLength - 1):
			validatorPattern = validatorPatterns[self.validatorRules[i]]
			validatorMessage = validatorMessages[self.validatorRules[i]]
			searchObject = re.search(validatorPattern, self.validatorInput)
			if (searchObject):
				validatorMessage = "{{" + validatorMessage + "}}"
				self.validatorMessage = self.validatorMessage + "\n" + validatorMessage

		# last rule is the rule of the accepted pattern

		validatorPattern = validatorPatterns[self.validatorRules[self.validatorsRulesLength - 1]]
		validatorMessage = validatorMessages[self.validatorRules[self.validatorsRulesLength - 1]]
		searchObject = re.search(validatorPattern, self.validatorInput)
		if not (searchObject):
			validatorMessage = "{{" + validatorMessage + "}}"
			self.validatorMessage = self.validatorMessage + "\n" + validatorMessage

		self.validatorMessage = re.sub('^\n', '', self.validatorMessage)
		return self.validatorMessage

class ValidatorsArray:
	def __init__(self, validatorsInputs, modelClass):
		self.validatorsInputs = validatorsInputs
		self.modelObject = modelClass()
		self.validatorsRulesDictionary = self.modelObject.validatorsRulesDictionary()
		self.validatorsArrayCondition = True
		self.validatorsArrayMessage = ""

	def run(self):
		for validatorsRulesKey in self.validatorsRulesDictionary:
			try:
				# validators inputs names (=equal=) validators rules dictionary keys names
				validatorInput = self.validatorsInputs[validatorsRulesKey]
				validatorRules = self.validatorsRulesDictionary[validatorsRulesKey]
				validator = Validator(validatorInput,validatorRules)
				validatorMessage = validator.run()
			except (MultiValueDictKeyError):
				validatorInput = ""
				validatorMessage = "{{Missing input}}"
			if(validatorMessage):
				validatorMessage = self.htmlMessage(validatorsRulesKey, validatorInput, validatorMessage)
				self.validatorsArrayMessage = self.validatorsArrayMessage + "\n\n" + validatorMessage
		# complete the html table tags
		if(self.validatorsArrayMessage):
			self.validatorsArrayMessage = "<table class='validationTable'><thead></thead><tfoot></tfoot><tbody>" \
			                              + self.validatorsArrayMessage \
			                              + "\n\n</tbody></table>"
		return self.validatorsArrayMessage

	def textMessage(self, validatorsRulesKey, validatorInput, validatorMessage):
		validatorMessage = re.sub('{{', '\t> ', validatorMessage)
		validatorMessage = re.sub('}}', '', validatorMessage)
		validatorMessage = " * Input\t: " + validatorsRulesKey + "\n" \
		                   + " * Value\t: " + validatorInput + "\n" \
		                   + validatorMessage
		return validatorMessage

	def htmlMessage(self, validatorsRulesKey, validatorInput, validatorMessage):
		validatorMessage = re.sub('{{', '<tr><td>', validatorMessage)
		validatorMessage = re.sub('}}', '</td></tr>', validatorMessage)
		validatorMessage = "<tr><th> * Input : " + validatorsRulesKey + "</th></tr>\n" \
		                   "<tr><th> * Value : " + validatorInput + "</th></tr>\n" \
		                   + validatorMessage
		return validatorMessage