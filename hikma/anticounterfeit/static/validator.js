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
		for(i=0; i<this.validatorsRulesLength-1; i++){
			validatorPattern			= validatorPatterns[this.validatorRules[i]];
			validatorPatternRegEx		= new RegExp(validatorPattern);
			validatorMessage			= validatorMessages[this.validatorRules[i]];
			if(validatorPatternRegEx.test(this.value)){
				this.validatorResult	= false;
				this.validatorMessage	= validatorMessage;
				this.checkLastRule		= false;
				break;
			}
		}
		if(this.checkLastRule) {
			validatorPattern = validatorPatterns[this.validatorRules[this.validatorsRulesLength-1]];
			validatorPatternRegEx		= new RegExp(validatorPattern);
			validatorMessage			= validatorMessages[this.validatorRules[this.validatorsRulesLength-1]];
			if (validatorPatternRegEx.test(this.value)) { //true
				this.validatorResult	= true;
				this.validatorMessage	= "";
			} else {
				this.validatorResult	= false;
				this.validatorMessage	= validatorMessage;
			}
		}
		var parent = this.inputElement.parent();
		if (parent.children("div.Validator").length>0) {
			parent.children("div.Validator").children("span.Validator").html(this.validatorMessage);
		} else {
			$("<div class='Validator'><span class='Validator'>" + this.validatorMessage + "</span></div>").insertBefore(this.inputElement);
			//parent.html("<div class='Validator'><span class='Validator'>" + this.validatorMessage	+ "</span></div>" + parent.html());
		}
		return this.validatorResult;
	};
};
function validatorArray() {
	validatorArrayCondition = true;
	$("[validator]").each(function(){
		validatorArrayCondition = validatorArrayCondition && new Validator($(this)).run();
		return validatorArrayCondition;
	});
	alert(validatorArrayCondition);
};
function validatorRun(){
	if(onPageLoad){
		$("[validator]").each(function(){new Validator($(this)).run();});
	};
	$("[validator]").on(validatorEvents, function(){new Validator($(this)).run();});
	$("[validatorArray='']").click(validatorArray);
};