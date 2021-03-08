import os.path
path = os.getenv('HOME') + '/yifyDB/movie_data'
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
import json
# for n in range(num_files):
for n in range(num_files):
    try:
        p=onlyfiles[n]
        completeName = os.path.join(path, str(p))
        if os.path.isfile(completeName):
            with open(completeName) as f:
                data = json.load(f)
                movie_id = data['movie_details']['movie']['id']
                if 'small_cover_image' in data['movie_details']['movie']:
                    small_img = data['movie_details']['movie']['small_cover_image']
                else:
                    small_img = "/assets/img/small alt.jpg"
                if 'large_cover_image' in data['movie_details']['movie']:
                    large_img = data['movie_details']['movie']['large_cover_image']
                else:
                    large_img = "/assets/img/large alt.jpg"
                movie_name = data['movie_details']['movie']['title']
                movie_title = movie_name.replace(':', '')
                movie_title = movie_title.replace("'", "")
                movie_title = movie_title.replace('*', '')
                movie_title = movie_title.replace('[', '')
                movie_title = movie_title.replace('-', '')
                movie_title = movie_title.replace(']', '')
                movie_name = str(movie_name)
                year = data['movie_details']['movie']['year']
                lan = data['movie_details']['movie']['language']
                if 'genres' in data['movie_details']['movie']:
                    genres = data['movie_details']['movie']['genres']
                    genres = ' / '.join(genres)
                    gen_len = len(genres)
                else:
                    genres = ""
                    gen_len = 0
                # genre = {}
                # for g in range(gen_len):
                #     genre[g] = genres[g]
                #     print(genres)
                rating = data['movie_details']['movie']['rating']
                imdb_id = data['movie_details']['movie']['imdb_code']
                desc_prefix = "Download "+movie_title+" in HD Quality. "
                desc_prefix_len = len(desc_prefix)
                remain_desc_size = 160 - desc_prefix_len
                description = data['movie_details']['movie']['description_full']
                desc = description.replace(':', '')
                desc = desc.replace('"', '')
                desc = desc.replace("'", "")
                desc = desc.replace('[', '')
                desc = desc.replace(']', '')
                desc = desc.replace('-', '')
                desc = desc.replace('*', '')
                desc = desc.replace('\n', '')
                desc = desc[:remain_desc_size]
                print(desc)
                if 'torrents' in data['movie_details']['movie']:
                    torrents = data['movie_details']['movie']['torrents']
                    torrents_len = len(torrents)
                    torrents_quality = {}
                    torrents_type = {}
                    torrents_size = {}
                    torrents_hash = {}
                    torrents_url = {}
                    for t in range(torrents_len):
                        torrents_quality[t] = data['movie_details']['movie']['torrents'][t]['quality']
                        torrents_type[t] = data['movie_details']['movie']['torrents'][t]['type']
                        torrents_size[t] = data['movie_details']['movie']['torrents'][t]['size']
                        torrents_hash[t] = data['movie_details']['movie']['torrents'][t]['hash']
                        torrents_url[t] = data['movie_details']['movie']['torrents'][t]['url']
                else:
                    torrents = ""
                    torrents_len = 0
                tor_modal = ''
                anchor_var = ''
                for i in range(torrents_len):
                    # anchor_var += '<a href="'+ torrents_hash[i] +'" class="avalable_variant">'+ torrents_quality[i] +'.'+ torrents_type[i] +'</a>'
                    torrents_type[i] = torrents_type[i].upper()
                    if torrents_quality[i] == "720p":
                        quality = "https://yts.mx/assets/images/website/720p-quality.svg"
                    elif torrents_quality[i] == "1080p":
                        quality = "https://yts.mx/assets/images/website/1080p-quality.svg"
                    elif torrents_quality[i] == "3D":
                        quality = "https://yts.mx/assets/images/website/3D-quality.svg"
                    elif torrents_quality[i] == "2160p":
                        quality = "https://yts.mx/assets/images/website/2160p-quality.svg"
                    else:
                        quality = ""
                    import urllib.parse
                    f = urllib.parse.quote_plus(movie_name)
                    traker = "&tr=udp://open.demonii.com:1337/announce&tr=udp://tracker.openbittorrent.com:80&tr=udp://tracker.coppersurfer.tk:6969&tr=udp://glotorrents.pw:6969/announce&tr=udp://tracker.opentrackr.org:1337/announce&tr=udp://torrent.gresille.org:80/announce&tr=udp://p4p.arenabg.com:1337&tr=udp://tracker.leechers-paradise.org:6969"
                    tor_modal += '''<div class="modal-torrent">
                      <div class="modal-quality" id="modal-quality-720p"><img src="'''+ quality +'''" alt=""></div>
                        <p class="quality-size">'''+ torrents_type[i] +'''</p>
                        <br>
                        <p>File size</p>
                        <br>
                        <p class="quality-size">'''+ torrents_size[i] +'''</p>
                        <br>
                        <a href="'''+ torrents_url[i] +'''" class="download_btn_main"><img class="download_logo" src="/assets/img/download-logo-white.png">Download</a>
                        <a href="magnet:?xt=urn:btih:'''+ torrents_hash[i] +'''&dn='''+ f +''''''+ traker +'''" class="magnet-download"><img class="magnet-link" src="https://yts.mx/assets/images/website/magnet.svg"></a>
                      </div>'''

                    anchor_var += '<a href="magnet:?xt=urn:btih:'+ torrents_hash[i] +'&dn='+ f +''+ traker +'" class="avalable_variant">'+ torrents_quality[i] +'.'+ torrents_type[i] +'</a>'
                # print(anchor_var)

                yt_trailer_code = data['movie_details']['movie']['yt_trailer_code']
                screenshot1 = data['movie_details']['movie']['large_screenshot_image1']
                screenshot2 = data['movie_details']['movie']['large_screenshot_image2']
                screenshot3 = data['movie_details']['movie']['large_screenshot_image3']
                if 'cast' in data['movie_details']['movie']:
                    cast = data['movie_details']['movie']['cast']
                    cast_len = len(cast)
                    cast_name = {}
                    cast_imdb = {}
                    for c in range(cast_len):
                        cast_name[c] = data['movie_details']['movie']['cast'][c]['name']
                        cast_imdb[c] = data['movie_details']['movie']['cast'][c]['imdb_code']
                else:
                    cast = ""
                    cast_len = 0
                cast_p_tag = ''
                for i in range(cast_len):
                    cast_p_tag += '<p>'+ cast_name[i] +'</p>'
                suggestions = data['movie_suggestions']['movies']
                suggestions_len = len(suggestions)
                sug_medium_cover_image = {}
                sug_url = {}
                sug_id = {}
                for s in range(suggestions_len):
                    sug_medium_cover_image[s] = data['movie_suggestions']['movies'][s]['medium_cover_image']
                    sug_url[s] = data['movie_suggestions']['movies'][s]['url']
                    sug_id[s] = data['movie_suggestions']['movies'][s]['id']
                import webbrowser
                message="""---
layout: default
title: {movie_title}
permalink: movies/{movie_id}/{movie_title}-{year}
description: {desc_prefix}{desc}
---

<div class="movie_page">
<div class="container">
  <div class="movie_poster_info flex-box no-m">
    <div class="movie_poster">
      <img class="movie_poster_img" src={large_img}>
    </div>
    <div class="movie_info">
      <h1 class="movie_title">{movie_name}</h1>
      <div class="year_lan flex-box">
          <h3 class="release_year">{year}</h3>
          <span class=language>{lan}</span>
      </div>
      <div class="genre_group flex-box">
        <h3 class="genre">{genres}</h3>
      </div>
      <a class="rating flex-box" href="https://www.imdb.com/title/{imdb_id}/?ref_=hm_tpks_tt_2_pd_tp1_cp" rel="noopener noreferrer nofollow target="_blank">
        <img class="imdb_logo_img" src="/assets/img/IMDB_Logo.svg" alt="IMDb Rating">
        <h3 class="rating_digit">{rating}</h3><img class="rating-star" src="/assets/img/star.svg">
      </a>
      <div class="description">
        <h4 class="description_heading">Description</h4>
        <p class="movie_description_para">
          {description}
        </p>
      </div>
      <a class="subtitles" href="https://yifysubtitles.org/movie-imdb/{imdb_id}" rel="noopener noreferrer nofollow" target="_blank">
        <img class="download_logo" src="/assets/img/download-logo-white.png">Download Subtitles
      </a>
    </div>
  </div>
  <div class="movie_poster_info no-dt">
    <div class="movie_poster">
      <img class="movie_poster_img" src="{large_img}">
    </div>
    <div class="movie_info">
      <h1 class="movie_title">{movie_name}</h1>
      <h3 class="release_year">{year}</h3>
      <div class="genre_group flex-box">
        <h3 class="genre">{genres}</h3>
      </div>
      <div class="rating flex-box">
        <img class="imdb_logo_img" src="/assets/img/IMDB_Logo.svg" alt="IMDb Rating">
        <h3 class="rating_digit">{rating}</h3><img class="rating-star" src="/assets/img/star.svg">
      </div>
    </div>
  </div>

  <div class="download_btn flex-box no-m no-t">
    <a onclick="openDownloadModal()" class="download_btn_main"><img class="download_logo" src="/assets/img/download-logo-white.png">Download</a>
    <div class="available_downloads flex-box">
      <div class="available_in">Available in: </div>
      {anchor_var}
    </div>
  </div>
  <div class="available_downloads flex-box no-d">
    <a href="#" class="avalable_variant"><img class="download_logo" src="/assets/img/download-logo-white.png">720p.WEB</a>
    <a href="#" class="avalable_variant"><img class="download_logo" src="/assets/img/download-logo-white.png">1080p.WEB</a>
  </div>
  <div class="subtitle_button_section flex-box no-dt">
    <a class="subtitles" href="https://yifysubtitles.org/movie-imdb/tt1715873" rel="noopener noreferrer nofollow" target="_blank">
      <img class="download_logo" src="/assets/img/download-logo-white.png">Download Subtitles
    </a>
  </div>
  <div class="description no-dt">
    <h4 class="description_heading">Description</h4>
    <p class="movie_description_para">
      {description}
    </p>
  </div>
  <div class="download-modal" id="download-modal">
    <span class="close-download-modal cursor" onclick="closeDownloadModal()">&times;</span>
    <div class="download-modal-content">
      <h3 class="download_title">Select Movie Quality</h3>
      <div class="download-modal-data flex-box">
        {tor_modal}
      </div>
    </div>
  </div>
  <div class="social_media_share flex-box">
    <a href="https://www.facebook.com/sharer/sharer.php?u={{{{site.my_domain}}}}{{{{page.url}}}}" class="social_media" target="_blank" rel="noopener noreferrer nofollow"><img class="facebook" src="/assets/img/023-facebook.svg"></a>
    <a href="http://www.reddit.com/submit?url={{{{site.my_domain}}}}{{{{page.url}}}}" class="social_media" target="_blank" rel="noopener noreferrer nofollow"><img class="reddit" src="/assets/img/072-reddit.svg"></a>
    <a href="https://twitter.com/intent/tweet?text={{{{site.my_domain}}}}{{{{page.url}}}}" class="social_media" target="_blank" rel="noopener noreferrer nofollow"><img class="twitter" src="/assets/img/twitter.svg"></a>
    <a class="social_media copy-link-logo no-m no-t"><img class="copy-link" src="/assets/img/link-symbol.svg"><span class="tooltiptext">Copy to clipboard</span></a>
    <a id="share_logo" class="social_media share-logo no-d"><svg id="Capa_1" fill="#fff" enable-background="new 0 0 512 512" height="512" viewBox="0 0 512 512" width="512" xmlns="http://www.w3.org/2000/svg"><path d="m391 332c-24.15 0-46.107 9.564-62.288 25.1l-96.254-59.633c5.492-12.728 8.542-26.747 8.542-41.467s-3.05-28.739-8.543-41.466l96.254-59.633c16.182 15.535 38.139 25.099 62.289 25.099 49.626 0 90-40.374 90-90s-40.374-90-90-90-90 40.374-90 90c0 14.651 3.521 28.495 9.758 40.732l-94.001 58.238c-19.276-23.184-48.321-37.97-80.757-37.97-57.897 0-105 47.103-105 105s47.103 105 105 105c32.436 0 61.481-14.786 80.757-37.97l94.001 58.238c-6.237 12.237-9.758 26.081-9.758 40.732 0 49.626 40.374 90 90 90s90-40.374 90-90-40.374-90-90-90zm0-302c33.084 0 60 26.916 60 60s-26.916 60-60 60-60-26.916-60-60 26.916-60 60-60zm-255 301c-41.355 0-75-33.645-75-75s33.645-75 75-75 75 33.645 75 75-33.645 75-75 75zm255 151c-33.084 0-60-26.916-60-60s26.916-60 60-60 60 26.916 60 60-26.916 60-60 60z"/></svg></a>

  </div>
  <div class="trailer_screens flex-box no-t">
    <a class="trailer_link video-banner js-trigger-video-modal" href="https://www.youtube.com/watch?v={yt_trailer_code}" data-youtube-id="{yt_trailer_code}"><img id="img1" class="screenshot trailer" src="{screenshot1}"><svg version="1.1" class="play-button" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve"><polygon style="fill:#FFFFFF;" points="187.368,146.928 187.368,355.8 382.992,251.368 "/><path style="fill:#FB4443;" d="M256,0.376C114.616,0.376,0,114.824,0,256s114.616,255.624,256,255.624S512,397.176,512,256S397.384,0.376,256,0.376z M184.496,146.928l195.624,104.44L184.496,355.8V146.928z"/></svg></a>

    <a class="screenshot_link" onclick="openModal();currentSlide(2)"><img id="img2" class="screenshot" src="{screenshot2}"></a>

    <a class="screenshot_link" onclick="openModal();currentSlide(3)"><img id="img3" class="screenshot" src="{screenshot3}"></a>

  </div>
  <div class="modal" id="myModal">
    <span class="close cursor" onclick="closeModal()">&times;</span>
    <div class="modal-content">
      <div class="mySlides">
        <img style="width:100%" src="{screenshot1}">
      </div>
      <div class="mySlides">
        <img style="width:100%" src="{screenshot2}">
      </div>
      <div class="mySlides">
        <img style="width:100%" src="{screenshot3}">
      </div>
      <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
    </div>
  </div>
  <div class="trailer_screens no-d">
    <a class="trailer_link video-banner js-trigger-video-modal" href="https://www.youtube.com/watch?v={yt_trailer_code}" data-youtube-id="{yt_trailer_code}"><img id="img1" class="screenshot trailer" src="{screenshot1}"><svg version="1.1" class="play-button" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 512 512" style="enable-background:new 0 0 512 512;" xml:space="preserve"><polygon style="fill:#FFFFFF;" points="187.368,146.928 187.368,355.8 382.992,251.368 "/><path style="fill:#FB4443;" d="M256,0.376C114.616,0.376,0,114.824,0,256s114.616,255.624,256,255.624S512,397.176,512,256S397.384,0.376,256,0.376z M184.496,146.928l195.624,104.44L184.496,355.8V146.928z"/></svg></a>

    <a class="screenshot_link" onclick="openModal();currentSlide(2)"><img id="img2" class="screenshot" src="{screenshot2}"></a>

    <a class="screenshot_link" onclick="openModal();currentSlide(3)"><img id="img3" class="screenshot" src="{screenshot3}"></a>
  </div>
  <div class="crew_cast flex-box">
    <div class="cast crew_cast_child">
      <h3>Cast</h3>
      {cast_p_tag}
    </div>
  </div>
  <div class="similar_movies_container">
    <h4>Similar Movies</h4>
    <div class="similar_movies flex-box">
      <a class="similar_movie_link" href="/movies/{sug_id[0]}"><img src="{sug_medium_cover_image[0]}"></a>
      <a class="similar_movie_link" href="/movies/{sug_id[1]}"><img src="{sug_medium_cover_image[1]}"></a>
      <a class="similar_movie_link" href="/movies/{sug_id[2]}"><img src="{sug_medium_cover_image[2]}"></a>
      <a class="similar_movie_link" href="/movies/{sug_id[3]}"><img src="{sug_medium_cover_image[3]}"></a>
    </div>
  </div>
</div>
</div>

<section class="video-modal">

    <!-- Modal Content Wrapper -->
    <div
         id="video-modal-content" class="video-modal-content"
     >

       <!-- iframe -->
       <iframe
          id="youtube"
          width="100%"
          height="100%"
          frameborder="0"
          allow="autoplay"
          allowfullscreen
          src=
        ></iframe>



        <a
        	href="#"
        	class="close-video-modal"
        >
        	<!-- X close video icon -->
          <svg
            version="1.1"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            x="0"
            y="0"
            viewBox="0 0 32 32"
            style="enable-background:new 0 0 32 32;"
            xml:space="preserve"
            width="24"
            height="24"
          >

            <g id="icon-x-close">
                <path fill="#ffffff" d="M30.3448276,31.4576271 C29.9059965,31.4572473 29.4852797,31.2855701 29.1751724,30.980339 L0.485517241,2.77694915 C-0.122171278,2.13584324 -0.104240278,1.13679247 0.52607603,0.517159487 C1.15639234,-0.102473494 2.17266813,-0.120100579 2.82482759,0.477288136 L31.5144828,28.680678 C31.9872448,29.1460053 32.1285698,29.8453523 31.8726333,30.4529866 C31.6166968,31.0606209 31.0138299,31.4570487 30.3448276,31.4576271 Z" id="Shape"></path>
                <path fill="#ffffff" d="M1.65517241,31.4576271 C0.986170142,31.4570487 0.383303157,31.0606209 0.127366673,30.4529866 C-0.12856981,29.8453523 0.0127551942,29.1460053 0.485517241,28.680678 L29.1751724,0.477288136 C29.8273319,-0.120100579 30.8436077,-0.102473494 31.473924,0.517159487 C32.1042403,1.13679247 32.1221713,2.13584324 31.5144828,2.77694915 L2.82482759,30.980339 C2.51472031,31.2855701 2.09400353,31.4572473 1.65517241,31.4576271 Z" id="Shape"></path>
            </g>

          </svg>
        </a>

    </div><!-- end modal content wrapper -->


    <!-- clickable overlay element -->
    <div class="overlay"></div>


</section>
            <g id="icon-x-close">
                <path fill="#ffffff" d="M30.3448276,31.4576271 C29.9059965,31.4572473 29.4852797,31.2855701 29.1751724,30.980339 L0.485517241,2.77694915 C-0.122171278,2.13584324 -0.104240278,1.13679247 0.52607603,0.517159487 C1.15639234,-0.102473494 2.17266813,-0.120100579 2.82482759,0.477288136 L31.5144828,28.680678 C31.9872448,29.1460053 32.1285698,29.8453523 31.8726333,30.4529866 C31.6166968,31.0606209 31.0138299,31.4570487 30.3448276,31.4576271 Z" id="Shape"></path>
                <path fill="#ffffff" d="M1.65517241,31.4576271 C0.986170142,31.4570487 0.383303157,31.0606209 0.127366673,30.4529866 C-0.12856981,29.8453523 0.0127551942,29.1460053 0.485517241,28.680678 L29.1751724,0.477288136 C29.8273319,-0.120100579 30.8436077,-0.102473494 31.473924,0.517159487 C32.1042403,1.13679247 32.1221713,2.13584324 31.5144828,2.77694915 L2.82482759,30.980339 C2.51472031,31.2855701 2.09400353,31.4572473 1.65517241,31.4576271 Z" id="Shape"></path>
            </g>

          </svg>
        </a>

    </div><!-- end modal content wrapper -->


    <!-- clickable overlay element -->
    <div class="overlay"></div>


</section>""".format(**locals())
        filename = f"movies/{movie_id}.html"
        file = open(filename,"w")
        file.write(message)
        file.close()
        print('No: {0} is {1}'.format(n, movie_name))
    except Exception as e:
        print(e)
        continue
    # break
