function variableValidator (inputElement) {
	this.inputElement				= inputElement;
	this.validationRule				= new RegExp(this.inputElement.attr("validator"));
	this.validationMessage			= this.inputElement.attr("validatorMessage");
	this.validationResult			= false;

	this.validateData = function() {
		if (this.validationRule.test(this.inputElement.val())) { //true
			this.validationResult	= true;
			this.validationMessage	= "";
		} else {
			this.validationResult	= false;
		}
		var parent = this.inputElement.parent();
		if (parent.children("div.variableValidator").length>0) {
			parent.children("div.variableValidator").children("span.variableValidator").html(this.validationMessage);
		} else {
			$("<div class='variableValidator'><span class='variableValidator'>" + this.validationMessage + "</span></div>").insertBefore(this.inputElement);
			//parent.html("<div class='variableValidator'><span class='variableValidator'>" + this.validationMessage	+ "</span></div>" + parent.html());
		}
		return this.validationResult;
	};

	this.getValidationResult	= function() { return this.validationResult; };
	this.getValidationMessage	= function() { return this.validationMessage; };
};

function arrayValidator (variableValidatorArray) {
	this.variableValidatorArray = variableValidatorArray || [];
	this.arrayValidatorResult	= "True";
	
	this.validateArrayValidator = function() {
		for (arrayValidatorIndex = 0; arrayValidatorIndex < this.variableValidatorArray.length; arrayValidatorIndex++) {
			this.arrayValidatorResult = this.arrayValidatorResult && this.variableValidatorArray[arrayValidatorIndex].validateData();
		}
		return this.arrayValidatorResult;
	};
	
	this.arrayValidatorAddItem = function(arrayValidatorItem) {
		this.variableValidatorArray.push(arrayValidatorItem);
		//this.variableValidatorArray[variableValidatorArray.length] = arrayValidatorItem;
	};
	
};
function validateDataFunction(){
	$("[validator]").each(function(){
		var vv = new variableValidator($(this));
		vv.validateData();
	});
	
	$("[validator]").on("change input keyup paste propertychange", function(){
		var vv = new variableValidator($(this));
		vv.validateData();
	});
};
function validateArrayValidatorFunction() {
	var av = new arrayValidator();
	$("[validator]").each(function(){
		var vv = new variableValidator($(this));
		vv.validateData();
		av.arrayValidatorAddItem(vv);
	});
	alert(av.validateArrayValidator());
};
