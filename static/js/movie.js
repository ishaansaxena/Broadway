$('.btn-add').click(function(e) {
    e.preventDefault();
    request_uri = "add";
    $.ajax({
        type: "POST",
        url: request_uri,
        success: function() {
            location.reload();
        }
    });
});

$('.btn-remove').click(function(e) {
    e.preventDefault();
    request_uri = "remove";
    $.ajax({
        type: "POST",
        url: request_uri,
        success: function() {
            location.reload();
        }
    });
});
