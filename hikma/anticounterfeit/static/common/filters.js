$(document).ready(function(){
	/*validatorCodeStart*/
	validatorRun();
	/*validatorCodeEnd*/

	var operatorSelectHTML = '<select id="operator" validator="Empty,Any" validatorSignature="201601111631"><option value="">Operators</option></select>';
	$('select#field').change(function(){
		$('#operator').html(operatorSelectHTML);
		var operators = $('select#field > option:selected').attr('operators');
		//alert((operatorsDictionariesDictionary["string"])["Is"])
		var operatorsDictionary = operatorsDictionariesDictionary[operators];
		for (operatorKey in operatorsDictionary){
			$('#operator').append('<option value="' + operatorsDictionary[operatorKey] + '">' + operatorKey + '</option>');
		};
		var validator = $('select#field > option:selected').attr('validator');
		$('#searchValue').attr('validator', validator);
	});
	$('input[type=button]#addFilter').click(function(){
		if (validatorArray("201601111631")) {
			var fieldText = $("select#field option:selected").text();
			var field = $('select#field').val();
			var operator = $('select#operator').val();
			var searchValue = $('input[type=text]#searchValue').val();
			var filterSelectID = 'select#' + field;
			var filter = operator + ' ' + searchValue
			if (!$(filterSelectID).length) {
				var filterSelect = $('<select></select>').attr('id', field);
				var labelOption = $('<option></option>').val('');
				labelOption.text(fieldText);
				filterSelect.append(labelOption);
				$('div#filters').append(filterSelect);
				$(filterSelectID).change(function() {
					if ($(filterSelectID + '> option:selected').val() != '') {
						var removeFilter = confirm('Are you sure, you need to delete filter "' + filter + '"');
						if (removeFilter) { $(filterSelectID + '> option:selected').remove(); }
						var hasOption = false;
						$(filterSelectID + '> option').each(function() {
							if ($(this).val() != '') {
								hasOption = true;
							}
						});
						if (!hasOption) { $(filterSelectID).remove(); }
					}
				});
			}
			if ($(filterSelectID + '> option[value="' + filter + '"]').index() == -1) {
				var filterOption = $('<option></option>').val(filter);
				filterOption.text(filter);
				$(filterSelectID).append(filterOption);
			} else {
				alert('Duplicated entry');
			}
			$('select#field > option[value=""]').prop('selected', 'selected');
			$("#operator").html(operatorSelectHTML);
			$('input[type=text]#searchValue').val('');
		}
	});
	$('input[type=button]#runFilters').click(function(){
		var filters = {};
		$("div.filterWidget > div.filters > select").each(function(){

			var fieldFiltersArray = "";
			var key = $(this).attr('id');
			$(this).find('option').each(function(){
				if ($(this).val()) { fieldFiltersArray = fieldFiltersArray + "::,::" + $(this).val() }
			});
			fieldFiltersArray = fieldFiltersArray.replace(/^::,::/, "");
			filters[key] = fieldFiltersArray;
		});
		alert(filters["count"]);
		$.post("/anticounterfeit/urn/filters/", filters, function(data, status){
			if (new RegExp("^Error:").test(data)) {
				var myWindow = window.open("", "Add Unique Random Numbers Validator", "width=400, height=300, scrollbars=yes");
				data = data.replace(/Error:/, "");
				myWindow.document.write(data);
			}
			else { myWindow.document.write(data);
			}
			//alert(data)
			//alert("Status: " + status);
		});
	});
});
var operatorsDictionariesDictionary = {
	"string": {"Is": "==", "Is Not": "!=", "Contains": "**", "Not Contains": "!*"},
	"number": {"Equal": "==", "Less Than": "<<", "Greater Than": ">>", "Less Than Or Equal": "=<", "Greater Than Or Equal": ">="},
}