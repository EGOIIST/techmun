import json
import csv
from sklearn.cluster import KMeans
import numpy as np

def cluster_maker():
    f = open('result.json').read()

    pep_data = json.loads(f)

    # open a file for writing

    people_data = open('PeopleData.csv', 'w')

    # create the csv writer object

    csvwriter = csv.writer(people_data)

    count = 0
    for pep in pep_data:
        if count == 0:
            header = pep_data[pep].keys()
            csvwriter.writerow(header)
            count += 1

        csvwriter.writerow(pep_data[pep].values())
        
    people_data.close()


def kmeansalgorithm():
   # X = np.array([[1, 2], [1, 4], [1, 0],
         # [4, 2], [4, 4], [4, 0]])
    
    f = open('PeopleData.csv','r')
    l = f.readlines()
    f.close()
    f = open('PeopleDataNew.csv',"w")
    for i in l:
        if i != "movie_theater,amusement_park,park,night_club,zoo,aquarium,stadium,bowling_alley,art_gallery,museum,airport,bar,spa,jewelry_store,bus_station,subway_station,train_station,casino\n" and i != "\n":
           f.write(i)
    f.truncate()
    f.close()

    f = open('PeopleDataNew.csv',"r")
    lines_of_people = f.readlines()
    counter = 0
    size_of_people = len(lines_of_people)

    result_gesamt = [None]*size_of_people
    for i in lines_of_people:  
        zwsch = [x for x in i.split(',')]
        zwsch[17] = zwsch[17].rstrip()
        for j in range(0, 18):
            zwsch[j] = int(zwsch[j])
        result_gesamt[counter] = zwsch
        if counter < 30:
           counter += 1
           
        else:
            break

    X = np.array(result_gesamt)
    kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
    #print(kmeans.labels_)
    #print(kmeans.predict([[24, 12, 25, 56, 23, 45, 12, 35, 29, 11, 40, 32, 22, 34, 1, 23, 7, 3]]))
    return kmeans.predict([[24, 12, 25, 56, 23, 45, 12, 35, 29, 11, 40, 32, 22, 34, 1, 23, 7, 3]])[0]



if __name__ == "__main__":
    kmeansalgorithm()                
