$('.search').click(function() {
    $('.search-view').fadeIn();
});

$('.search-view').click(function() {
    $('.search-view').fadeOut();
}).children().click(function(e) {
  return false;
});

$('.search-field').on('enterKey', function(e) {
    var query = $(this).val();
    var request_uri = "/q/" + slugify(query) + "/";
    window.location.href = request_uri;
});

$('.search-field').on('keypress', function(e) {
    if (e.keyCode === 13) {
        $(this).trigger('enterKey');
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
