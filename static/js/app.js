
var apiLocation = 'api/v1/';
var pastWeek = [];

$(document).ready( function() {
	getData();
});

function getData() {
	$.ajax({
		url: apiLocation + '0/0',
		type: 'GET',
		dataType: 'json',
		contentType: 'application/json',
		success: function(json) {
			console.log(json);
			fileeLatest(json.instances[0]);
			fillStats(json['core-stats']);
			fillTable(json.instances, $('.past-week'));
		}
	});
}

function fillLatest(latest) {
	$('.latest-data .temperature').html( (latest.temp_instance/1000).toFixed(1) + '&deg;c' );
	$('.latest-data .date').html( latest.temp_date );
}

function fillStats(stats) {
	$('.max').html(stats.temp_max);
	$('.min').html(stats.temp_min);
	$('.avg').html(stats.temp_avg);
}

function fillTable(instances, table) {
	$.each(instances, function(i, val) {
		var html = '<tr>';
		html += '<td>' + val.temp_date + '</td>';
		html += '<td>' + (val.temp_instance/1000).toFixed(1) + '&deg;c</td>';
		html += '</tr>';
		table.append(html);
	});
}