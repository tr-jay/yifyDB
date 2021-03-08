# import requests
# headers = {'cookie': '__cfduid=d163ce528b96ef59ccaec19ee437c42bd1611740242; __atssc=google%3B5; PHPSESSID=arkp9754mc08606pu13hupgsdt; __cf_bm=e9b0528d44f67ad9215b079fb771517ef6f8831b-1611826673-1800-AUn6j4jGDzBjLLCamq7QTuN2bgww4VEJdJDv3VApPD1uI6SaqQzv/YSRD2U9WZctaZE6t/enJmOJPhKdlodIBV+pffzpeh/l1KpRVAInwBEDKL/cAd53J9nIyky+ym5kew==; __atuvc=12%7C4; __atuvs=601285f1e3ad5130000', 'origin': 'https://yts.mx/', 'referer': 'https://yts.mx/', 'sec-fetch-site': 'same-origin'}
# result=requests.get('https://yts.mx/api/v2/list_movies.json')
# print('res')
# res=result.json()
# import json
# with open("data.json", "w") as outfile:
#     json.dump(res, outfile)
#     print('data updated')


import requests

url = 'https://yts.mx/api/v2/list_movies.json'
# headers = {'cookie': '__cfduid=d163ce528b96ef59ccaec19ee437c42bd1611740242; __atssc=google%3B5; PHPSESSID=arkp9754mc08606pu13hupgsdt; __cf_bm=e9b0528d44f67ad9215b079fb771517ef6f8831b-1611826673-1800-AUn6j4jGDzBjLLCamq7QTuN2bgww4VEJdJDv3VApPD1uI6SaqQzv/YSRD2U9WZctaZE6t/enJmOJPhKdlodIBV+pffzpeh/l1KpRVAInwBEDKL/cAd53J9nIyky+ym5kew==; __atuvc=12%7C4; __atuvs=601285f1e3ad5130000', 'origin': 'https://yts.mx/', 'referer': 'https://yts.mx/', 'sec-fetch-site': 'same-origin'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers=headers)
# print(response.content)
res=response.json()
import json
with open("data.json", "w") as outfile:
    json.dump(res, outfile)
print('data updated')
