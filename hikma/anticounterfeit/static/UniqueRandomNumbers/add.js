$(document).ready(function(){
    $("select#UniqueRandomNumber-Product").load("/anticounterfeit/product");
	$("input#URN-add").click(addClick);
	/*validatorCodeStart*/
	validatorRun();
	/*validatorCodeEnd*/
});
function addClick() {
    postArray = {}
    $("[name]").each(function(){postArray[$(this).attr("name")] = $(this).val();});
    alert(postArray["URN-uniqueRandomNumbersCount"]);
}
