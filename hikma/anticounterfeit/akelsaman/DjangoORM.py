class DjangoORM:

	def __init__(self, modelClass):
		self.modelObject = self.modelClass()
		self.modelObjectFieldsNames = self.modelObject._meta.get_fields()

	def insert(self, fieldsInputs):
		for key in range (1, self.modelObjectFieldsNames.__len__()):
			fieldName = self.modelObjectFieldsNames[key].name


	def update(self):
		pass

	def drop(self):
		pass

	def select(self):
		pass