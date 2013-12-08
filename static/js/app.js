$(document).ready( function() {




	var d = new Date().getTime();
	$.ajax({
		url: 'api/v1/0/' + d,
		type: 'GET',
		success: function(json) {
			console.log(json)
		}
	})





});