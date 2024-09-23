import requests
import json
import csv

url = "https://rickandmortyapi.com/api/character"

result= [["name", "location", "image"]]
while url:
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()
            
        result  += [ [i["name"],i["location"]["name"],i["image"]] for i in data["results"] 
                    if i["species"] == "Human" 
                    if i["status"] == "Alive" 
                    if i["origin"]["name"].split()[0] == "Earth" ]
        
        url = data["info"]["next"]
        
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        break

print(result)

with open('characters.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)
