import os.path
path = os.getenv('HOME') + '/abc/data'
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])

for n in range(num_files):
# for n in range(1):
    import json
    p=n+1
    with open(path+'/page '+str(p)+'.json') as f:
        data = json.load(f)
        for m in range(20):
        # for m in range(5):
            save_path = './movie_data'
            # save_path = './test_data'
            movie_id = data['data']['movies'][m]['id']
            completeName = os.path.join(save_path, str(movie_id)+'.json')
            if os.path.isfile(completeName):
                print (completeName+' already exists')
            else:
                for attempt in range(10):
                    try:
                        import requests
                        result=requests.get('https://yts.mx/api/v2/movie_details.json?movie_id='+str(movie_id)+'&with_images=true&with_cast=true')
                        res = result.json()
                        result2=requests.get('https://yts.mx/api/v2/movie_suggestions.json?movie_id='+str(movie_id))
                        res2 = result2.json()
                        import json
                        final = {'movie_details': res['data'], 'movie_suggestions': res2['data']}
                        with open(completeName, "w") as outfile:
                            json.dump(final, outfile)
                        print(completeName+' added succesfully')
                    except Exception as e:
                        print(e)
                        continue
                    break
