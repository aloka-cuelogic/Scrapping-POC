$(function() {
    $('#getcityarea').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
            url: "/crawler/get_results/",
            type: "POST",
            data: {
                city_id: $('#id_city').val(),
                locality_id: $('#id_locality').val()
            },
            success: function(response) {
                response = JSON.parse(response);
                $('#resultdisplay').html("");
                $('#resultdisplay').append('<h3>' + "Properties on Rent" + '<h3>');
                $.each(response, function(i, jsonobjectlist) {
                    $.each(jsonobjectlist['fields'], function(key, value) {
                        $('#resultdisplay').append('<p>' + key + ':' + value + '</p>');
                    });
                    $('#resultdisplay').append('-------------------------');
                });
            },
            error: function(data) {
                $('#resultdisplay').html("");
            },
        });
    })
})
