$('.btn-follow').click(function() {
    request_uri = "follow";
    $.ajax({
        type: "POST",
        url: request_uri,
        success: function() {
            location.reload();
        }
    });
});

$('.btn-unfollow').click(function() {
    request_uri = "unfollow";
    $.ajax({
        type: "POST",
        url: request_uri,
        success: function() {
            location.reload();
        }
    });
});
