$('.btn-follow').click(function() {
    request_uri = "follow";
    console.log(request_uri);
    $.post(request_uri);
});

$('.btn-unfollow').click(function() {
    request_uri = "unfollow";
    console.log(request_uri);
    $.post(request_uri);
});
