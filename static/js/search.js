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

$('.heart-movie').click(function(e) {
    e.preventDefault();
    var $this = $(this);
    var request_uri = $this.attr("href");
    var aC, rC;
    if ($this.hasClass("btn-outline-danger")) {
        request_uri += "/add";
        aC = "btn-danger";
        rC = "btn-outline-danger";
    } else {
        request_uri += "/remove"
        aC = "btn-outline-danger";
        rC = "btn-danger";
    }
    console.log(request_uri);
    $.ajax({
        type: "POST",
        url: request_uri,
        success: function() {
            $this.removeClass(rC);
            $this.addClass(aC);
        }
    });
});
