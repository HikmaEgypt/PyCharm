$(document).ready(function(){
    $("select#product").load("/anticounterfeit/product/");
    var dt  = new Date();
    yyyy    = dt.getFullYear()
    mm      = ((dt.getMonth() + 1)<10?"0" + (dt.getMonth() + 1):(dt.getMonth() + 1));
    dd      = (dt.getDate()<10?"0" + dt.getDate():dt.getDate());
    HH      = (dt.getHours()<10?"0" + dt.getHours():dt.getHours());
    MM      = (dt.getMinutes()<10?"0" + dt.getMinutes():dt.getMinutes());
    $("input[type=text]#dateAndTime").val(yyyy + "." + mm + "." + dd + " " + HH + ":" + MM);
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
    $.post("/anticounterfeit/urn/add/", postArray, function(data, status){
        if (new RegExp("^Error:").test(data)) {
            var myWindow = window.open("", "Add Unique Random Numbers Validator", "width=400, height=300, scrollbars=yes");
            data = data.replace(/Error:/, "");
            myWindow.document.write(data);
        }
        else { $("input#id").val(data);
        }
        //alert(data)
        //alert("Status: " + status);
    });

}