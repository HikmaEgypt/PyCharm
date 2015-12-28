#how to:
#   ake = Validator(ANYVARIABLE, "Empty,Dshs,Spcs")
#   print(ake.run())

import re
from .validatorSettings import validatorPatterns, validatorMessages

class Validator:

	def __init__(self, validatorInput, validatorRules):
		self.validatorInput			    = validatorInput
		self.validatorRules			    = validatorRules.split(",")
		self.validatorsRulesLength      = self.validatorRules.__len__()
		self.validatorMessage           = ""

	def run(self):
		for i in range(0, self.validatorsRulesLength - 1):
			validatorPattern            = validatorPatterns[self.validatorRules[i]]
			validatorMessage            = validatorMessages[self.validatorRules[i]]
			searchObject                = re.search(validatorPattern, self.validatorInput)
			if(searchObject):
				self.validatorMessage   = self.validatorMessage + "\n" + validatorMessage

			# last rule is the rule of the accepted pattern

			validatorPattern            = validatorPatterns[self.validatorRules[self.validatorsRulesLength - 1]]
			validatorMessage            = validatorMessages[self.validatorRules[self.validatorsRulesLength - 1]]
			searchObject                = re.search(validatorPattern, self.validatorInput)
			if not (searchObject):
				self.validatorMessage   = self.validatorMessage + "\n" + validatorMessage

		return self.validatorMessage

	def runForHTML(self):
		validatorMessage = self.run

class ValidatorsArray:

	def __init__(self, validatorsInputs, modelClass):
		self.validatorsInputs               = validatorsInputs
		self.modelObject                    = modelClass()
		self.validatorsRules                = self.modelObject.validatorsRules()
		self.validatorsArrayCondition       = True
		self.validatorsArrayMessages        = ""

	def run(self):
		for validatorRules in self.validatorsRules:
			validator                       = Validator(self.validatorsInputs[validatorRules], self.validatorsRules[validatorRules])
			self.validatorsArrayMessages    = self.validatorsArrayMessages + validator.run()

			#validatorArrayCondition = validatorArrayCondition && v;
			#validatorArrayCondition = validatorArrayCondition && new Validator($(this)).run(); //stopped after first validator !!!
		return self.validatorsArrayMessages