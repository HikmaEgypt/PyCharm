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

# ============================================================================ #
class Validator:
	def __init__(self, validatorInput, validatorRules):
		self.validatorInput = validatorInput
		self.validatorRules = validatorRules.split(",")
		self.validatorsRulesLength = self.validatorRules.__len__()
		self.validatorMessage = ""
# ---------------------------------------------------------------------------- #
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
class ValidatorsDictionary:
	def __init__(self):
		self.validatorsInputsDictionary = ""
		self.validatorsInputsFormat = ""
		self.fieldsValidatorsRulesDictionary = ""
		self.validatorsDictionaryMessage = ""
		self.checkMissingInputs = True
# ---------------------------------------------------------------------------- #
	def run(self, validatorsInputsDictionary, validatorsInputsFormat, fieldsValidatorsRulesDictionary,
	        checkMissingInputs, validatorsDictionaryMessageFormat):
		self.validatorsInputsDictionary = validatorsInputsDictionary
		self.validatorsInputsFormat = validatorsInputsFormat
		self.fieldsValidatorsRulesDictionary = fieldsValidatorsRulesDictionary
		self.checkMissingInputs = checkMissingInputs
		self.validatorsDictionaryMessage = ""
		for fieldName in self.fieldsValidatorsRulesDictionary:
			if self.fieldsValidatorsRulesDictionary[fieldName] is not "":
				validatorRules = self.fieldsValidatorsRulesDictionary[fieldName]
				validatorsMessages=""
				try:
					if self.validatorsInputsFormat is "Dictionary":
						validatorInput = self.validatorsInputsDictionary[fieldName]
						validator = Validator(validatorInput,validatorRules)
						validatorMessage = validator.run()
						if validatorMessage:
							validatorsMessages = "{{h2:: * Value\t: " + validatorInput + "::h2}}\n" + validatorMessage
					elif self.validatorsInputsFormat is "ArraysDictionary":
						validatorsInputsArray = self.validatorsInputsDictionary[fieldName].split("::,::")
						for validatorInput in validatorsInputsArray:
							validator = Validator(validatorInput[3:],validatorRules)
							validatorMessage = validator.run()
							if validatorMessage:
								validatorsMessages = validatorsMessages + \
								                     "\n{{h2:: * Value\t: " + validatorInput[3:] + "::h2}}\n" + \
								                     validatorMessage
				# if you are using MultiValueDictKeyError, from django.utils.datastructures import MultiValueDictKeyError
				except KeyError:
					if checkMissingInputs:
						validatorsMessages = "{{h2:: * Value\t: ::h2}}\n" + "{{MessageLine::Missing input::MessageLine}}"
				if(validatorsMessages):
					validatorsMessages = "{{h1:: * Input\t: " + fieldName + "::h1}}\n" + validatorsMessages
					self.validatorsDictionaryMessage = self.validatorsDictionaryMessage + "\n\n" + validatorsMessages
		if self.validatorsDictionaryMessage:
			if validatorsDictionaryMessageFormat=="text": self.textMessage()
			elif validatorsDictionaryMessageFormat=="html": self.htmlMessage()
			return self.validatorsDictionaryMessage
# ---------------------------------------------------------------------------- #
	def textMessage(self):
		tagsDictionary = {
			'{{h1::': '',
			'::h1}}': '',
			'{{h2::': '',
			'::h2}}': '',
			'{{MessageLine::': '\t>',
			'::MessageLine}}': '',
		}
		for tag in tagsDictionary:
			self.validatorsDictionaryMessage = re.sub(tag, tagsDictionary[tag], self.validatorsDictionaryMessage)
# ---------------------------------------------------------------------------- #
	def htmlMessage(self):
		tagsDictionary = {
			'{{h1::': '\t<tr><th class="h1">',
			'::h1}}': '</th></tr>',
			'{{h2::': '\t<tr><th class="h2">',
			'::h2}}': '</th></tr>',
			'{{MessageLine::': '\t<tr><td>',
			'::MessageLine}}': '</td></tr>',
		}
		for tag in tagsDictionary:
			self.validatorsDictionaryMessage = re.sub(tag, tagsDictionary[tag], self.validatorsDictionaryMessage)

		self.validatorsDictionaryMessage = "<table class='validationTable'><thead></thead><tfoot></tfoot><tbody>" \
		                              + self.validatorsDictionaryMessage \
		                              + "\n\n</tbody></table>"

		self.validatorsDictionaryMessage = '''Error:
		<html>
			<head>
				<title>Add Unique Random Numbers Validator</title>
				<meta charset="UTF-8">
				<meta name="viewport" content="width=device-width, initial-scale=1.0">
				<LINK REL=StyleSheet HREF="/static/common/css.css" TYPE="text/css">
			</head>
			<body>
		''' + self.validatorsDictionaryMessage + '''
			</body>
		</html>'''