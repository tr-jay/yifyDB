import os.path
path = os.getenv('HOME') + '/abc/movie_data'
num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
import json
print(num_files)
num_files = num_files + 1
print(num_files)
for n in range(num_files):
    print (n)
    # try:
    j = 1
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
            # if 'title' in data['movie_details']['movie']:
            movie_name = data['movie_details']['movie']['title']
            movie_name = str(movie_name)
            year = data['movie_details']['movie']['year']
            file_name = "search_master.json"
            if( n == 0 ):
                res = {"movie_info": [{'movie_id': movie_id, 'title': movie_name, 'poster': small_img, 'year': year}]}
                with open(file_name, "w") as outfile:
                    json.dump(res, outfile)
                # with open(file_name) as json_file:
                #     data = json.load(json_file)
                j = 2
            else:
                def write_json(data, filename=file_name):
                    with open(filename,'w') as f:
                        json.dump(data, f, indent=2)

                with open(file_name) as json_file:
                    data = json.load(json_file)

                    temp = data['movie_info']
                    res = {'movie_id': movie_id, 'title': movie_name, 'poster': small_img, 'year': year}
                    print (n)
                    print(res)
                    temp.append(res)
                write_json(data)
    else:
        print('There is no such file named '+p)
    # except Exception as e:
    #     print(e)
    #     continue
    # break
