$('#searchform input[name="searchform"]').on("keyup", function(e) {
	var term = $('#searchform input[name="searchform"]').val();
	console.log(term);
});

$(window).scroll(function() {
  if ($(document).scrollTop() > 50) {
    $('nav.navbar').addClass('shrink');
  } else {
    $('nav.navbar').removeClass('shrink');
  }
});