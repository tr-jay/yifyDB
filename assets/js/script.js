$(document).ready(function() {
$('#search-box').on('input',function(e){
  var keycode = (e.keyCode ? e.keyCode : e.which);
    if(keycode == '13'){
        console.log('You pressed a "enter" key in textbox');
    }
  $("#search-results").html("");
  var searchField = $("#search-box").val();
  var expression = new RegExp(searchField, "i");
  if(searchField == "")
  {
    $("#search-results").addClass("no-disp");
  }
  else {
    $("#search-results").removeClass("no-disp");
    $.getJSON('/search_master.json',function(data){
      jsonData = data.movie_info;
      //console.log(jsonData);
      var j = 0;
      $.each(jsonData, function(key, value){
        //console.log(value.title);
        if (j < 7) {
        if(value.title.search(expression) != -1) {
          console.log(value.movie_id);
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
console.log('second last: '+second_last_page);

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
  console.log(plus_four);
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
  var expression = new RegExp(searchField, "i")
  // var looping = jsonData.movie_info;
  // $($(looping).get().reverse()).each(function(index){
  // var id = this.movie_id;
  // var title = this.title;
  // var s_img = this.poster;
  // var year = this.year;
  // var txtValue, input, a, i, ul, li;
  // var k = 1;
  // var imgs = '<img src="`+s_img+`">'
  // input = document.getElementById("search-box");
  // var filter = input.value.toUpperCase();
  // if (filter == "") {
  //   //console.log('filter empty');
  //   $('#search-results').addClass("no-disp");
  //   $("li").addClass("no-disp");
  // }
  // else {
  //   ul = document.getElementById("search-results");
  //   li = ul.getElementsByTagName("li");
  // if(k <= 1) {
  //   $("#search-results").append(`
  //     <li class="search_movie_block">
  //         <a href="/movies/`+id+`" class="flex-box search_movie_link">
  //             <img src="`+s_img+`">
  //             <div class="search_movie_info">
  //               <h4 class="search_movie_title">`+title+`</h4>
  //               <p>`+year+`</p>
  //             </div>
  //         </a>
  //       </li>
  //   `);
  //   k++;
  // }
  //
  // $("li").addClass("no-disp");
  //   var j = 0;
  //   for (var i=0; i < li.length; i++) {
  //     a = li[i];
  //     var txtValue = a.innerText;
  //     if (txtValue.toUpperCase().indexOf(filter) > -1) {
  //       $('#search-results').removeClass("no-disp");
  //       $("li").removeClass("no-disp");
  //       if (j < 5){
  //         li[i].style.display = "list-item";
  //       }
  //       else {
  //         li[i].style.display = "none";
  //       }
  //       j++;
  //       //console.log(j);
  //     }
  //     else {
  //       li[i].style.display = "none";
  //     }
  //   }
  // }
  //
  //
  // });

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
var random_page = Math.floor(Math.random() * 100);
console.log(random_page);
var settings = {
"type": "GET",
"datatype": "json",
"async": true,
"url" : "/home page.json"
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
              <div class="movie-rating"><img class="rating-star" src="/assets/img/star.svg"><div class="rating-digit">`+rating+`/10</div></div>
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


// $.getJSON('/movie_by_name/A.json',function(data){
//   jsonData = data.movie_info;
//   console.log(jsonData);
  // var looping = jsonData.movie_info;
  // $($(looping).get().reverse()).each(function(index){
  // var id = this.movie_id;
  // var title = this.title;
  // var s_img = this.poster;
  // var year = this.year;
  // var txtValue, input, a, i, ul, li;
  // var k = 1;
  // var imgs = '<img src="`+s_img+`">'
  // input = document.getElementById("search-box");
  // var filter = input.value.toUpperCase();
  //   ul = document.getElementById("search-results");
  //   li = ul.getElementsByTagName("li");
  // if(k <= 1) {
  //   $("#search-results").append(`
  //     <li class="search_movie_block">
  //         <a href="/movies/`+id+`" class="flex-box search_movie_link">
  //             <img src="`+s_img+`">
  //             <div class="search_movie_info">
  //               <h4 class="search_movie_title">`+title+`</h4>
  //               <p>`+year+`</p>
  //             </div>
  //         </a>
  //       </li>
  //   `);
  //   k++;
  // }
  // $("li").addClass("no-disp");
  // }
  // $('#search-box').on('input',function(e){
  //   $("#search-results").html("");
  //   var searchField = $("#search-box").val();
  //   var expression = new RegExp(searchField, "i");
  //   if(searchField == "")
  //   {
  //     $("#search-results").addClass("no-disp");
  //   }
  //   else {
  //     $("#search-results").removeClass("no-disp");
  //     $.getJSON('search_master.json',function(data){
  //       jsonData = data.movie_info;
  //       //console.log(jsonData);
  //       var j = 0;
  //       $.each(jsonData, function(key, value){
  //         //console.log(value.title);
  //         if (j < 5) {
  //         if(value.title.search(expression) != -1) {
  //           $("#search-results").append(`
  //               <li class="search_movie_block">
  //                   <a href="/movies/`+value.id+`" class="flex-box search_movie_link">
  //                       <img src="`+value.poster+`">
  //                       <div class="search_movie_info">
  //                         <h4 class="search_movie_title">`+value.title+`</h4>
  //                         <p>`+value.year+`</p>
  //                       </div>
  //                   </a>
  //                 </li>
  //             `);
  //             j++;
  //         }
  //
  //       }
  //       })
  //     });
  //   }
  //
  //
  //   //search();
  // });

//});

});

}
pages();



// function search(){
//   console.log('key pressed');
// $(document).ready(function() {
//
// //var looping = jsonData.movie_info;
// $("#search-results").html("");
// $($(looping).get().reverse()).each(function(index){
// var id = this.movie_id;
// var title = this.title;
// var s_img = this.poster;
// var year = this.year;
// var txtValue, input, filter, a, i, ul, li;
// var k = 1;
// var imgs = '<img src="`+s_img+`">'
// input = document.getElementById("search-box");
// filter = input.value.toUpperCase();
// if(filter == "")
// {
//
// }
// else {
//   ul = document.getElementById("search-results");
//   li = ul.getElementsByTagName("li");
//
// if(k <= 1) {
// //  if(results <= 5) {
//   $("#search-results").append(`
//     <li class="search_movie_block">
//         <a href="/movies/`+id+`" class="flex-box search_movie_link">
//             <img src="`+s_img+`">
//             <div class="search_movie_info">
//               <h4 class="search_movie_title">`+title+`</h4>
//               <p>`+year+`</p>
//             </div>
//         </a>
//       </li>
//   `);
//     //results++;
// //  }
//   k++;
// }
//   for (i=0; i < li.length; i++) {
//     a = li[i];
//     txtValue = a.innerText;
//     if (txtValue.toUpperCase().indexOf(filter) > -1) {
//       $('#search-results').removeClass("no-disp");
//       if (i < 5){
//         li[i].style.display = "list-item";
//       }
//       else {
//         li[i].style.display = "none";
//       }
//     }
//     else {
//       $('#search-results').addClass("no-disp");
//       li[i].style.display = "none";
//     }
//   }
// }
//
// });
// // }
// });
// }





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

// $('#share_logo').on('click', () => {
//   try {
//     navigator.share({
//         title: 'Web Share API Draft',
//         text: 'Take a look at this spec!',
//         url: 'https://developer.mozilla.org',
//       })
//       .then(() => console.log('Successful share'))
//       .catch((error) => console.log('Error sharing', error));
//   } catch(e) {
//     console.log(e);
//   }
// });
