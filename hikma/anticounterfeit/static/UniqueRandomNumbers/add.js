$(document).ready(function(){
    $("select#product").load("/anticounterfeit/product/");
	$("input#add").click(addClick);
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
    //alert(postArray["URN-internalOrExternal"]);
    $.post("/anticounterfeit/UniqueRandomNumbers/add/", postArray, function(data, status){
        //if (new RegExp("^Error").test(data)) { alert(data); } else { $("[window='add,result']").html(data); }
        alert(data);
        //alert("Status: " + status);
    });

}
