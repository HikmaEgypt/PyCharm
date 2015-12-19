function Validator (inputElement) {
	this.inputElement				= inputElement;
	this.value						= this.inputElement.val();
	this.validatorAttributeValue	= this.inputElement.attr("validator");
	this.validatorRules				= this.validatorAttributeValue.split(",");
	this.validatorsRulesLength		= this.validatorRules.length;
	this.validatorMessage			= "";
	this.checkLastRule				= true;
	this.validatorResult			= false;

	this.run = function() {
		for(var i=0; i<this.validatorsRulesLength-1; i++){
			var validatorPattern		= validatorPatterns[this.validatorRules[i]];
			var validatorPatternRegEx	= new RegExp(validatorPattern);
			var validatorMessage		= validatorMessages[this.validatorRules[i]];
			if(validatorPatternRegEx.test(this.value)){
				this.validatorResult	= false;
				this.validatorMessage	= validatorMessage;
				this.checkLastRule		= false;
				break;
			}
		}
		if(this.checkLastRule) {
			var validatorPattern 		= validatorPatterns[this.validatorRules[this.validatorsRulesLength-1]];
			var validatorPatternRegEx	= new RegExp(validatorPattern);
			var validatorMessage		= validatorMessages[this.validatorRules[this.validatorsRulesLength-1]];
			if (validatorPatternRegEx.test(this.value)) { //true
				this.validatorResult	= true;
				this.validatorMessage	= "";
			} else {
				this.validatorResult	= false;
				this.validatorMessage	= validatorMessage;
			}
		}
		var parent = this.inputElement.parent();
		if (parent.children("div.validator").length>0) {
			parent.children("div.validator").children("span.validator").html(this.validatorMessage);
		} else {
			$("<div class='validator'><span class='validator'>" + this.validatorMessage + "</span></div>").insertBefore(this.inputElement);
			//parent.html("<div class='validator'><span class='validator'>" + this.validatorMessage	+ "</span></div>" + parent.html());
		}
		return this.validatorResult;
	};
};
function validatorArray() {
	var validatorArrayCondition = true;
	$("[validator]").each(function(){
		var v = new Validator($(this)).run();
		validatorArrayCondition = validatorArrayCondition && v;
		//validatorArrayCondition = validatorArrayCondition && new Validator($(this)).run(); //stopped after first validator !!!
	});
	return validatorArrayCondition;
};
function validatorRun(){
	if(onPageLoad){
		$("[validator]").each(function(){new Validator($(this)).run();});
	};
	$("[validator]").on(validatorEvents, function(){new Validator($(this)).run();});
	//$("[validatorArray='']").click(validatorArray);
};