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
				validatorMessage = "{{MessageLine::Missing input::MessageLine}}"
			if(validatorMessage):
				validatorMessage = "{{h1:: * Input\t: " + validatorsRulesKey + "::h1}}\n" + \
				                   "{{h2:: * Value\t: " + validatorInput + "::h2}}\n" + \
				                   validatorMessage
				self.validatorsArrayMessage = self.validatorsArrayMessage + "\n\n" + validatorMessage
		if(self.validatorsArrayMessage): self.validatorsArrayMessage = self.htmlMessage(self.validatorsArrayMessage)
		return self.validatorsArrayMessage

	def textMessage(self, validatorMessage):
		validatorMessage = re.sub('{{h1::', '', validatorMessage)
		validatorMessage = re.sub('::h1}}', '', validatorMessage)
		validatorMessage = re.sub('{{h2::', '', validatorMessage)
		validatorMessage = re.sub('::h2}}', '', validatorMessage)
		validatorMessage = re.sub('{{MessageLine::', '\t>', validatorMessage)
		validatorMessage = re.sub('::MessageLine}}', '', validatorMessage)
		return validatorMessage

	def htmlMessage(self, validatorMessage):
		validatorMessage = re.sub('{{h1::', '\t<tr><th>', validatorMessage)
		validatorMessage = re.sub('::h1}}', '</th></tr>', validatorMessage)
		validatorMessage = re.sub('{{h2::', '\t<tr><th>', validatorMessage)
		validatorMessage = re.sub('::h2}}', '</th></tr>', validatorMessage)
		validatorMessage = re.sub('{{MessageLine::', '\t<tr><td>', validatorMessage)
		validatorMessage = re.sub('::MessageLine}}', '</td></tr>', validatorMessage)
		validatorMessage = "<table class='validationTable'><thead></thead><tfoot></tfoot><tbody>" \
		                              + validatorMessage \
		                              + "\n\n</tbody></table>"
		return validatorMessage