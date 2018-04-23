$('.btn-search').on('mousedown', function(e) {
    var query = $('.search-field').val();
    if (query.length > 0) {
        var request_uri = "/q/" + slugify(query) + "/";
        // console.log(request_uri);
        window.location.href = request_uri;
    }
});

$('.search-field').on('keypress', function(e) {
    if (e.keyCode === 13) {
        e.preventDefault();
        $('.btn-search').trigger('mousedown');
    }
});

function slugify(text) {
  return text.toString().toLowerCase()
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
    .replace(/^-+/, '')             // Trim - from start of text
    .replace(/-+$/, '');            // Trim - from end of text
}

$('.search-result').hide();
$('.movie').show();

$('.search-nav').click(function() {
    $('.search-result').hide();
    $('.search-nav').removeClass('active')
    $(this).addClass('active');
    var show = "." + $(this).attr("show");
    $(show).show();
});
