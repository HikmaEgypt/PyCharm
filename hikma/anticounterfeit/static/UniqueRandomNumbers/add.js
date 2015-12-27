$(document).ready(function(){
    $("select#URN-product").load("/anticounterfeit/product");
	$("input#URN-add").click(addClick);
	/*validatorCodeStart*/
	validatorRun();
	/*validatorCodeEnd*/
});
function addClick() {
    postArray = {}
    //$("[name]").each(function(){postArray[$(this).attr("name")] = $(this).val();});
    $("[name]").each(function(){
        if($(this).attr("type")=="radio"){
            if($(this).is(":checked")){
                postArray[$(this).attr("name")] = $(this).val();
            }
        } else {
            postArray[$(this).attr("name")] = $(this).val();
        }
    });
    alert(postArray["URN-internalOrExternal"]);

}
