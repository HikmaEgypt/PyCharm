$(document).ready(function(){
	$("select#product").load("/anticounterfeit/product");

	$("select#pharmacyState").load("/anticounterfeit/state");
	$("select#pharmacyState").change(pharmacyStateChange);
	$("select#pharmacyCity").change(pharmacyCityChange);
	$("select#pharmacy").change(pharmacyChange);

	$("select#doctorState").load("/anticounterfeit/state");
	$("select#doctorState").change(doctorStateChange);
	$("select#doctorCity").change(doctorCityChange);
	$("select#doctor").change(doctorChange);

	$("input#check").click(checkClick);

	/*validatorCodeStart*/
	validatorRun();
	/*validatorCodeEnd*/
});
function pharmacyStateChange() {
	$("input#pharmacy").hide();
	$("select#pharmacy").show();
	$("select#pharmacyCity").load("/anticounterfeit/"	+ $("#pharmacyState").val()	+ "/city");
	$("select#pharmacy").load("/anticounterfeit/0/pharmacy");
}
function pharmacyCityChange() {
	$("input#pharmacy").hide();
	$("select#pharmacy").show();
	$("select#pharmacy").load("/anticounterfeit/"	+ $("#pharmacyCity").val() + "/pharmacy");
}
function pharmacyChange(){
	if ($("select#pharmacy :selected").text() == "أخرى") {
		$("select#pharmacy").hide();
		$("input#pharmacy").show();
	}
}

function doctorStateChange() {
	$("input#doctor").hide();
	$("select#doctor").show();
	$("select#doctorCity").load("/anticounterfeit/" + $("#doctorState").val() + "/city");
	$("select#doctor").load("/anticounterfeit/0/doctor");
}
function doctorCityChange() {
	$("input#doctor").hide();
	$("select#doctor").show();
	$("select#doctor").load("/anticounterfeit/" + $("#doctorCity").val() + "/doctor");
}
function doctorChange(){
	if ($("select#doctor :selected").text() == "أخرى") {
		$("select#doctor").hide();
		$("input#doctor").show();
	}
}
function checkClick() {
	pharmacyValue	= ($("select#pharmacy").val()==0?$("input[type=text]#pharmacy").val():$("select#pharmacy").val());
	doctorValue		= ($("select#doctor").val()==0?$("input[type=text]#doctor").val():$("select#doctor").val());
	if(validatorArray("201601110106")){
		postArray = {
			product			: $("#product").val(),
			productCode		: $("#productCode").val(),
			checker			: $("#checker").val(),
			checkerMobile	: $("#checkerMobile").val(),
			checkerEmail	: $("#checkerEmail").val(),
			pharmacy		: $("#pharmacy").val(),
			doctor			: $("#doctor").val()
		}
		$.post("/anticounterfeit/result/", postArray, function(data, status){
			if (new RegExp("^Error").test(data)) { alert(data); } else { $("#bodyDiv").html(data); }
			//alert("Status: " + status);
		});
		/*$.get("/anticounterfeit/result/", function(data, status){
			alert("Data: " + data + "\nStatus: " + status);
			$("#bodyDiv").html(data)
		});*/
	}
}

