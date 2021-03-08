import requests
headers = {'cookie': '__cfduid=d163ce528b96ef59ccaec19ee437c42bd1611740242; __atssc=google%3B5; PHPSESSID=arkp9754mc08606pu13hupgsdt; __cf_bm=e9b0528d44f67ad9215b079fb771517ef6f8831b-1611826673-1800-AUn6j4jGDzBjLLCamq7QTuN2bgww4VEJdJDv3VApPD1uI6SaqQzv/YSRD2U9WZctaZE6t/enJmOJPhKdlodIBV+pffzpeh/l1KpRVAInwBEDKL/cAd53J9nIyky+ym5kew==; __atuvc=12%7C4; __atuvs=601285f1e3ad5130000', 'origin': 'https://yts.mx/', 'referer': 'https://yts.mx/', 'sec-fetch-site': 'same-origin'}
result=requests.get('https://yts.mx/api/v2/list_movies.json', headers=headers)
print('res')
res=result.json()
import json
with open("data.json", "w") as outfile:
    json.dump(res, outfile)
    print('data updated')
with open('data.json') as json_file:
    import math
    data = json.load(json_file)
    movie_count = data['data']['movie_count']
    page_count = movie_count / 20
    page_count = math.ceil(page_count)
    print (movie_count)
    for p in range(page_count):
        import os.path
        save_path = './json pages'
        page_no = p+1
        completeName = os.path.join(save_path, 'page '+str(page_no)+'.json')
        if os.path.isfile(completeName):
            print (completeName+' already exists')
        else:
            for attempt in range(5):
                try:
                    #import requests
                    result=requests.get('https://yts.mx/api/v2/list_movies.json?page='+str(p), headers=headers)
                    result.raise_for_status()
                    res=result.json()
                    import os.path


                    import json
                    with open(completeName, "w") as outfile:
                        json.dump(res, outfile)
                    print(completeName+' added succesfully')
                except Exception as e:
                    # Maybe set up for a retry, or continue in a retry loop
                    print(e)
                    continue
                break
