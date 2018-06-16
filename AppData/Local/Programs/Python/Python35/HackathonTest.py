import urllib.request
import json
from random import randint

def jsongenerating():
    jsonurl = urllib.request.urlopen("https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.json");
    text = json.loads(jsonurl.read().decode())
    text = text[0:30]

    sightseeing_list = ["amusement_park", "aquarium", "art_gallery",  "museum", "park", "stadium", "zoo"]
    nightlife_list = ["bowling_alley", "movie_theater", "night_club", "stadium"]
    extraordinary_list = ["bar", "casino", "jewelry_store", "spa"]
    mobility_list = ["airport", "bus_station", "subway_station", "train_station"]

    alltogether_list = sightseeing_list + nightlife_list + extraordinary_list + mobility_list
      

    jsondata = "{"
    for i in range(len((text))):
        jsondata += '\"' + text[i] + '"' + ": {"
        for j in range(len(alltogether_list)):
            jsondata += '"' + str(alltogether_list[j]) + '"' + ": " + str(randint(0, 50))
            jsondata += ","
        jsondata = jsondata[:-1]
        jsondata += "},"
    jsondata = jsondata[:-1]
    jsondata += "}"

    #n = json.dumps(jsondata)
    #print(n)
    a = json.loads(jsondata)
    print(a)
    with open('result.json', 'w') as fp:
        json.dump(a, fp)

if __name__ == "__main__":
    jsongenerating()
