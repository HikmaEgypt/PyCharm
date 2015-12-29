# how to:
#   ake = Validator(ANYVARIABLE, "Empty,Dshs,Spcs")
#   print(ake.run())

import re
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
				self.validatorMessage = self.validatorMessage + "\n" + validatorMessage

		# last rule is the rule of the accepted pattern

		validatorPattern = validatorPatterns[self.validatorRules[self.validatorsRulesLength - 1]]
		validatorMessage = validatorMessages[self.validatorRules[self.validatorsRulesLength - 1]]
		searchObject = re.search(validatorPattern, self.validatorInput)
		if not (searchObject):
			self.validatorMessage = self.validatorMessage + "\n" + validatorMessage

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
			# validators inputs names (=equal=) validators rules dictionary keys names
			validator = Validator(self.validatorsInputs[validatorsRulesKey],
			                      self.validatorsRulesDictionary[validatorsRulesKey])
			validatorMessage = validator.run()
			if(validatorMessage):
				validatorMessage = re.sub('\n', '\n\t > ', validatorMessage)
				validatorMessage = " * Input\t:" + validatorsRulesKey + "\n" \
				                   + " * Value\t:" + self.validatorsInputs[validatorsRulesKey] + "\n" \
				                   + validatorMessage
				self.validatorsArrayMessage = self.validatorsArrayMessage + "\n\n" + validatorMessage

		return self.validatorsArrayMessage

	def runHTML(self):
		for validatorsRulesKey in self.validatorsRulesDictionary:
			# validators inputs names (=equal=) validators rules dictionary keys names
			validator = Validator(self.validatorsInputs[validatorsRulesKey],
			                      self.validatorsRulesDictionary[validatorsRulesKey])
			validatorMessage = validator.run()

			# convert validator message from text to html
			if(validatorMessage):
				validatorMessage = re.sub('\n', '</td></tr>\n<tr><td>', validatorMessage)
				validatorMessage = "<tr><th> * Input : " + validatorsRulesKey + "</th></tr>\n" \
				                   "<tr><th> * Value : " + self.validatorsInputs[validatorsRulesKey] + "</th></tr>\n" \
				                   + validatorMessage + "</td></tr>"
				validatorMessage = re.sub('</th>\n</td></tr>', '</th>', validatorMessage)
				self.validatorsArrayMessage = self.validatorsArrayMessage + "\n" + validatorMessage

		# complete the html table tags
		if(self.validatorsArrayMessage):
			self.validatorsArrayMessage = re.sub('\n', '\n\t', self.validatorsArrayMessage)
			self.validatorsArrayMessage = "<table class='validationTable'><thead></thead><tfoot></tfoot><tbody>" \
			                              + self.validatorsArrayMessage \
			                              + "\n</tbody></table>"

		return self.validatorsArrayMessage