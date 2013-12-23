var pastWeek = [];

$(document).ready( function() {
	var d = new Date().getTime();
	$.ajax({
		url: 'api/v1/0/0',
		type: 'GET',
		dataType: 'json',
		contentType: 'application/json',
		success: function(json) {
			var latest = json.instances[0];
			$('.latest-data .temperature').html( (latest.temp_instance/1000).toFixed(1) + '&deg;c' );
			$('.latest-data .date').html( latest.temp_date );

			fillTable(json.instances, $('.past-week'));
		}
	});
});

function fillTable(instances, table) {
	$.each(instances, function(i, val) {
		var html = '<tr>';
		html += '<td>' + val.temp_date + '</td>';
		html += '<td>' + (val.temp_instance/1000).toFixed(1) + '&deg;c</td>';
		html += '</tr>';
		table.append(html);
	});
}