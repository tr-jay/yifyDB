import os.path
path = os.getenv('HOME') + '/abc/json pages'
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
import json
for n in range(num_files):
    # try:
    p=onlyfiles[n]
    completeName = os.path.join(path, str(p))
    p_len = len(p)
    q = p[:p_len -5]
    u = q[5:]
    print(u)
    if os.path.isfile(completeName):
        with open(completeName) as f:
            data = json.load(f)
            message="""---
layout: default
menu: false
date: '2021-01-29 01:53:59'
title: 'Browse Movies'
permalink: 'pages/{u}'
---
<div class="pagination flex-box">""".format(**locals())
            for i in range(20):
                movie_id = data['data']['movies'][i]['id']
                if 'medium_cover_image' in data['data']['movies'][i]:
                    medium_img = data['data']['movies'][i]['medium_cover_image']
                else:
                    medium_img = "/assets/img/medium alt.jpg"
                movie_name = data['data']['movies'][i]['title']
                movie_name = str(movie_name)
                year = data['data']['movies'][i]['year']
                rating = data['data']['movies'][i]['rating']
                if 'genres' in data['data']['movies'][i]:
                    genre_length = len(data['data']['movies'][i]['genres'])
                    genres1 = data['data']['movies'][i]['genres'][0]
                    genres = "<div>{genres1}</div>".format(**locals())
                    if (genre_length > 1):
                        genres2 = data['data']['movies'][i]['genres'][1]
                        genres += "<div>{genres2}</div>".format(**locals())
                if 'language' in data['data']['movies'][i]:
                    language = data['data']['movies'][i]['language']
                import webbrowser
                # print(p)
                message+="""
<article class="box-item">
  <div class="box-body">
      <a class="cover flex-box" href="/yifydb/movies/{movie_id}/{movie_name}-{year}">
              <img src="{medium_img}" width="100%" class="preload">
              <noscript>
                  <img src="{medium_img}" width="100%">
              </noscript>
              <div class="movie-rating"><img class="rating-star" src="/yifydb/assets/img/star.svg"><div class="rating-digit">{rating}/10</div></div>
              <div class="movie-rating pages_genre">{genres}</div>
      </a>
      <div class="box-info flex-box">
          <a class="post-link" href="/yifydb/movies/{movie_id}/{movie_name}-{year}">
              <h2 class="post-title">
                  {movie_name}
              </h2>
          </a>
          <div class="year_and_len flex-box">
              <p>{year}</p>
              <p class="pages_language">[{language}]</p>
          </div>
      </div>
  </div>
</article>

""".format(**locals())
            message+="""</div>
<div class="pages flex-box">
<div class="first_prev flex-box">
    <a id="first_page" class="page_no not_active_page" href="1">First</a>
    <a id="prev_page" class="page_no not_active_page" href="#">Previous</a>
</div>
    <div class="all_pages no-m flex-box">
            """
            for n in range(num_files):
                n = n+1
                message+="""<a id="page{n}" class="page_no page_number not_active_page no-disp" href="{n}">{n}</a>""".format(**locals())
            message+="""</div>
            <div class="last_next flex-box">
            <a id="next_page" class="page_no not_active_page" href="#">Next</a>
<a id="last_page" class="page_no not_active_page" href="#">Last</a>
</div>
</div>"""
            filename = f"pages/{q}.html"
            file = open(filename,"w")
            file.write(message)
            file.close()
        # print('No: {0} is {1}'.format(n, p))
    # except Exception as e:
    #     print(e)
    #     continue
    # break
