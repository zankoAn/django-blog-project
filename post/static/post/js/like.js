$("#btn-like, #btn-unlike").click(function(e){
  // like for detect user really want to like or unlike, yup thats it.
  var like_url = "/like/"
  var button = e.target
  var post_id = button.getAttribute("data-stat")

  $.ajax({
    url: like_url + post_id,
    method: "GET",
    data: {},
    success: function(data){
      $("#total-likes-"+post_id).text(data["like_count"]);
      $(button).attr({"class": data["class"]});
    }
  });
});
