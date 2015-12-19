function Validator (inputElement) {
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
		if (parent.children("div.validator").length>0) {
			parent.children("div.validator").children("span.validator").html(this.validationMessage);
		} else {
			$("<div class='validator'><span class='validator'>" + this.validationMessage + "</span></div>").insertBefore(this.inputElement);
			//parent.html("<div class='validator'><span class='validator'>" + this.validationMessage	+ "</span></div>" + parent.html());
		}
		return this.validationResult;
	};

	this.getValidationResult	= function() { return this.validationResult; };
	this.getValidationMessage	= function() { return this.validationMessage; };
};

function arrayValidator (ValidatorArray) {
	this.ValidatorArray = ValidatorArray || [];
	this.arrayValidatorResult	= "True";
	
	this.validateArrayValidator = function() {
		for (arrayValidatorIndex = 0; arrayValidatorIndex < this.ValidatorArray.length; arrayValidatorIndex++) {
			this.arrayValidatorResult = this.arrayValidatorResult && this.ValidatorArray[arrayValidatorIndex].validateData();
		}
		return this.arrayValidatorResult;
	};
	
	this.arrayValidatorAddItem = function(arrayValidatorItem) {
		this.ValidatorArray.push(arrayValidatorItem);
		//this.ValidatorArray[ValidatorArray.length] = arrayValidatorItem;
	};
	
};
function validateDataFunction(){
	/*$("[validator]").each(function(){
		var vv = new Validator($(this));
		vv.validateData();
	});*/
	
	//$("[validator]").on("change input keyup paste propertychange", function(){
	$("[validator]").on("change", function(){
		var vv = new Validator($(this));
		vv.validateData();
	});
};
function validateArrayValidatorFunction() {
	var av = new arrayValidator();
	$("[validator]").each(function(){
		var vv = new Validator($(this));
		vv.validateData();
		av.arrayValidatorAddItem(vv);
	});
	alert(av.validateArrayValidator());
};
