class DjangoORM:

	def __init__(self, modelClass):
		self.modelClass = modelClass
		self.modelObject = self.modelClass()
		self.modelObjectFieldsNames = self.modelObject._meta.get_fields()

	def insert(self, fieldsInputs):
		for key in range (2, self.modelObjectFieldsNames.__len__()):
			fieldName = self.modelObjectFieldsNames[key].name
			setattr(self.modelObject, fieldName, fieldsInputs[fieldName])
			#self.modelObject.fieldName = fieldsInputs[fieldName]
		self.modelObject.save()

	def update(self):
		pass

	def drop(self):
		pass

	def select(self):
		pass