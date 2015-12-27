function Validator (validatorInput) {
	this.validatorInput					= validatorInput;
	this.value							= this.validatorInput.val();
	this.validatorAttributeValue		= this.validatorInput.attr("validator");
	this.validatorRules					= this.validatorAttributeValue.split(",");
	this.validatorsRulesLength			= this.validatorRules.length;
	this.validatorMessage				= "";
	this.checkLastRule					= true;
	this.validatorResult				= false;

	this.run = function() {
		for (var i = 0; i < this.validatorsRulesLength - 1; i++) {
			var validatorPattern = validatorPatterns[this.validatorRules[i]];
			var validatorPatternRegEx = new RegExp(validatorPattern);
			var validatorMessage = validatorMessages[this.validatorRules[i]];
			if (validatorPatternRegEx.test(this.value)) {
				this.validatorResult = false;
				this.validatorMessage = validatorMessage;
				this.checkLastRule = false;
				break;
			}
		}
		if (this.checkLastRule) {
			var validatorPattern = validatorPatterns[this.validatorRules[this.validatorsRulesLength - 1]];
			var validatorPatternRegEx = new RegExp(validatorPattern);
			var validatorMessage = validatorMessages[this.validatorRules[this.validatorsRulesLength - 1]];
			if (validatorPatternRegEx.test(this.value)) { //true
				this.validatorResult = true;
				this.validatorMessage = "";
			} else {
				this.validatorResult = false;
				this.validatorMessage = validatorMessage;
			}
		}
		this.validatorInput.parent().children("div.validator").children("span.validator").html(this.validatorMessage);
		return this.validatorResult;
	};
};
function validatorArray() {
	var validatorArrayCondition = true;
	$("[validator]:visible").each(function(){
		var v = new Validator($(this)).run();
		validatorArrayCondition = validatorArrayCondition && v;
		//validatorArrayCondition = validatorArrayCondition && new Validator($(this)).run(); //stopped after first validator !!!
	});
	return validatorArrayCondition;
};
function validatorRun(){
	$("<div class='validator'><span class='validator'></span></div>").insertBefore($("[validator]"));
	if(onPageLoad){
		$("[validator]:visible").each(function(){new Validator($(this)).run();});
	};
	$("[validator]:visible").on(validatorEvents, function(){new Validator($(this)).run();});
};