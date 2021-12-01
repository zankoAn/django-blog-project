$("#share_post_link").click(function() {
  var copyText = document.getElementById("share_post_link");
  navigator.clipboard.writeText(copyText.baseURI);

  $('#copied').show();
  $('#copied').fadeOut(1000);

});
