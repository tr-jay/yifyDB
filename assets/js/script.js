$(document).ready(function() {
$('#search-box').on('input',function(e){
  var keycode = (e.keyCode ? e.keyCode : e.which);
  $("#search-results").html("");
  var searchField = $("#search-box").val();
  var expression = new RegExp(searchField, "i");
  if(searchField == "")
  {
    $("#search-results").addClass("no-disp");
  }
  else {
    $("#search-results").removeClass("no-disp");
    $.getJSON('/yifydb/search_master.json',function(data){
      jsonData = data.movie_info;
      //console.log(jsonData);
      var j = 0;
      $.each(jsonData, function(key, value){
        //console.log(value.title);
        if (j < 7) {
        if(value.title.search(expression) != -1) {
          $("#search-results").append(`
              <li class="search_movie_block">
                  <a href="/movies/`+value.movie_id+`/`+value.title+`-`+value.year+`" class="flex-box search_movie_link">
                      <img src="`+value.poster+`">
                      <div class="search_movie_info">
                        <h4 class="search_movie_title">`+value.title+`</h4>
                        <p>`+value.year+`</p>
                      </div>
                  </a>
                </li>
            `);
            j++;
        }

      }
      })
    });
  }


  //search();
});

$('#search').click(function() {
$('.search-wrapper').addClass("active");
$('.search-form').addClass("active");
});

$('.icon-remove-sign').click(function() {
$('.search-wrapper').removeClass("active");
$('.search-form').removeClass("active");
});

window.jsonData = [];

var pathname = window.location.pathname;
var path_len = pathname.length;
var current_page = pathname.slice(7, path_len);
var number_of_pages=$('.page_number').length;
$("#last_page").attr("href", number_of_pages);
var page = 'page';
var current_page_id = page.concat(current_page);
var last_page_id = page.concat(number_of_pages);
$("#" + current_page_id).removeClass("not_active_page");
$("#" + current_page_id).addClass("active_page");
$("#" + current_page_id).click(function() {
  event.preventDefault();
});

if (current_page != 1){
  var prev = current_page - 1;
  $("#prev_page").attr("href", prev);
}
else {
  $("#prev_page").addClass("no-disp");
  $("#first_page").addClass("no-disp");
  $("#page1").click(function() {
    event.preventDefault();
  });
}

if (current_page != number_of_pages) {
  var next = parseInt(current_page) + 1;
  $("#next_page").attr("href", next);
}
else {
  $("#next_page").addClass("no-disp");
  $("#last_page").addClass("no-disp");
  $("#"+last_page_id).click(function() {
    event.preventDefault();
  });
}

var second_last_page = parseInt(number_of_pages) - 1;
var third_last_page = parseInt(number_of_pages) - 2;
var fourth_last_page = parseInt(number_of_pages) - 3;
var fifth_last_page = parseInt(number_of_pages) - 4;

if (current_page == 1 || current_page == 2 || current_page == 3 || current_page == 4)
{
  for (var i = 1; i<=7; i++){
    var visible_page_num = i;
    var visible_page = page.concat(visible_page_num);
    $("#"+visible_page).removeClass("no-disp");
  }
  // $("#page1").removeClass("no-disp");
}

else if (current_page == number_of_pages || current_page == second_last_page || current_page == third_last_page || current_page == fourth_last_page){
  var nop = parseInt(number_of_pages);
  for (var i = nop; i>=(nop - 6); i--){
    var visible_page_num = i;
    var visible_page = page.concat(visible_page_num);
    $("#"+visible_page).removeClass("no-disp");
  }
}

else {
  var plus_four = parseInt(current_page) + 3;
  var minus_four = parseInt(current_page) - 3;
  for (var i = current_page; i<=plus_four; i++){
    var visible_page_num = i;
    var visible_page = page.concat(visible_page_num);
    $("#"+visible_page).removeClass("no-disp");
  }
  for (var i = current_page; i>=minus_four; i--){
    var visible_page_num = i;
    var visible_page = page.concat(visible_page_num);
    $("#"+visible_page).removeClass("no-disp");
  }
}
// console.log(next);

});

function search() {
  $("#search-results").html("");
  var searchField = $("#search-box").val();
  var expression = new RegExp(searchField, "i");
}

var $temp = $("<input>");
var $url = $(location).attr('href');

$(".copy-link").click(function() {
  $("body").append($temp);
  $temp.val($url).select();
  document.execCommand("copy");
  $temp.remove();
  $(".tooltiptext").html("URL coppied");
});

function pages(){
window.p = 1;
$(document).ready(function() {
var settings = {
"type": "GET",
"datatype": "json",
"async": true,
"url" : "/yifydb/home_page.json"
};

$.ajax(settings).done(function (data) {
window.data = data;
var looping = data.data.movies;
//$(".box-item").remove();
$(".row").append(`
  <div class="home_heading">
    <h1>Download YIFY movies: HD at smallest size</h1>
    <p>Welcome to YifyDB. Here you can browse and download YIFY movies in excellent 720p, 1080p, 2160p 4K and 3D quality, all at the smallest file size. YIFY Movies Torrents.</p>
    <hr>
  </div>
  `);
$($(looping).get().reverse()).each(function(index){
var id = this.id;
var title = this.title;
var url = this.url;
var medium_image_url = this.medium_cover_image;
var year = this.year;
var rating = this.rating;
var language = this.language;
var genres = this.genres;
var genres_length = genres.length;
if (genres_length > 1) {
  var genres1 = this.genres[0];
  var genres2 = this.genres[1];
  var genre = "<div>"+genres1+"</div><div>"+genres2+"</div>"
}
else {
  var genres1 = this.genres[0];
  var genre = "<div>"+genres1+"</div>"
}
$(".row").append(`
<article class="box-item">
  <div class="box-body">
      <a class="cover flex-box" href="/movies/`+id+`/`+title+`-`+year+`">
              <img src="`+medium_image_url+`" width="100%" class="preload">
              <noscript>
                  <img src="`+medium_image_url+`" width="100%">
              </noscript>
              <div class="movie-rating"><img class="rating-star" src="/yifydb/assets/img/star.svg"><div class="rating-digit">`+rating+`/10</div></div>
              <div class="movie-rating pages_genre">`+genre+`</div>
      </a>
      <div class="box-info">
          <a class="post-link" href="/movies/`+id+`/`+title+`-`+year+`">
              <h2 class="post-title">
                  `+title+`
              </h2>
          </a>
          <div class="year_and_len flex-box">
            <p class="description">`+year+`</p>
            <p class="pages_language">[`+language+`]</p>
          </div>
      </div>
  </div>
</article>
`);
});
});

});

}
pages();



function openDownloadModal() {
document.getElementById("download-modal").style.display = "block";
}

function closeDownloadModal() {
document.getElementById("download-modal").style.display = "none";
}

function openModal() {
document.getElementById("myModal").style.display = "block";
}

function closeModal() {
document.getElementById("myModal").style.display = "none";
}

var slideIndex = 1;
showSlides(slideIndex);


function plusSlides(n) {
showSlides(slideIndex += n);
}

function currentSlide(n) {
showSlides(slideIndex = n);
}

function showSlides(n) {
var i;
var slides = document.getElementsByClassName("mySlides");
var dots = document.getElementsByClassName("demo");
if (n > slides.length) {slideIndex = 1}
if (n < 1) {slideIndex = slides.length}
for (i = 0; i < slides.length; i++) {
slides[i].style.display = "none";
}
// for (i = 0; i < dots.length; i++) {
//   dots[i].className = dots[i].className.replace(" active", "");
// }
slides[slideIndex-1].style.display = "block";
}


$(document).ready(function(){


/* Toggle Video Modal
-----------------------------------------*/
function toggle_video_modal() {

  // Click on video thumbnail or link
  $(".js-trigger-video-modal").on("click", function(e){

      // prevent default behavior for a-tags, button tags, etc.
      e.preventDefault();

      // Grab the video ID from the element clicked
      var id = $(this).attr('data-youtube-id');

      // Autoplay when the modal appears
      // Note: this is intetnionally disabled on most mobile devices
      // If critical on mobile, then some alternate method is needed
      var autoplay = '?autoplay=1';

      // Don't show the 'Related Videos' view when the video ends
      var related_no = '&rel=0';

      // String the ID and param variables together
      var src = '//www.youtube.com/embed/'+id+autoplay+related_no;

      // Pass the YouTube video ID into the iframe template...
      // Set the source on the iframe to match the video ID
      $("#youtube").attr('src', src);

      // Add class to the body to visually reveal the modal
      $("body").addClass("show-video-modal noscroll");

  });

  // Close and Reset the Video Modal
  function close_video_modal() {

    event.preventDefault();

    // re-hide the video modal
    $("body").removeClass("show-video-modal noscroll");

    // reset the source attribute for the iframe template, kills the video
    $("#youtube").attr('src', '');

  }
  // if the 'close' button/element, or the overlay are clicked
  $('body').on('click', '.close-video-modal, .video-modal .overlay', function(event) {

      // call the close and reset function
      close_video_modal();

  });
  // if the ESC key is tapped
  $('body').keyup(function(e) {
      // ESC key maps to keycode `27`
      if (e.keyCode == 27) {

        // call the close and reset function
        close_video_modal();

      }
  });
}
toggle_video_modal();



});

let shareData = {
    title: 'MDN',
    text: 'Learn web development on MDN!',
    url: 'https://developer.mozilla.org',
  }

  const btn = document.querySelector('#share_logo');

  btn.addEventListener('click', () => {
    navigator.share(shareData)
      .then(() =>
        console.log('Successful share')
      )
      .catch((e) =>
        console.log('Error sharing', e)
      )
  });
