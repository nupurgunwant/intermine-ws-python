import requests
import yaml
from intermine.webservice import Service

def getInfo(mine):
    link="http://registry.intermine.org/service/instances/" + mine
    r=requests.get(link)

    dict=yaml.load(r.text)
    print("Description: " + dict["instance"]["description"])
    print("URL: " + dict["instance"]["url"])
    print("API Version: " + dict["instance"]["api_version"])
    print("Release Version: " + dict["instance"]["release_version"])
    print("InterMine Version: " + dict["instance"]["intermine_version"])
    print("Organisms: "),
    for organism in dict["instance"]["organisms"]:
        print(organism),
    print("Neighbours: "),
    for neighbour in dict["instance"]["neighbours"]:
        print(neighbour),

def getData(x):
    link = "http://www." + x + ".org/" + x + "/service"
    service=Service(link)
    query = service.new_query("DataSet")
    query.add_view("name", "url")
    list=[]

    for row in query.rows():
        try:
            list.append(row["name"])

        except:
            print ("No info available")
    list.sort()
    for i in range(len(list)):
        print("Name: " + list[i])


def getMines(organism):
    link="http://registry.intermine.org/service/instances"
    r=requests.get(link)

    dict=yaml.load(r.text)
    for i in range(len(dict["instances"])):
        for j in range(len(dict["instances"][i]["organisms"])):
            if (dict["instances"][i]["organisms"][j]==organism):
                print(dict["instances"][i]["name"])
            elif (dict["instances"][i]["organisms"][j]== " " + organism):
                print(dict["instances"][i]["name"])