import json
import pprint


def sortOnLong(dict):
    return dict["longitude"]


def code():

    print("Dit zijn de namen, codes en types van elk station:")

    longs = []
    with open("opdracht_7_4.json", "r") as file:
        data = json.load(file)

        for station in data.get("payload"):
            longitude = station.get("lng")
            name = station.get("namen")["lang"]
            longs.append({"name": name, "longitude": longitude})
            code = station.get("code")
            stationType = station.get("stationType")
            string = f"{name} - {code}   : {stationType}"
            print(string)

    longs.sort(key=sortOnLong)
    message = f"\nHet meest oostelijk gelegen station is: {longs[len(longs) -1].get("name")}"
    print(message)


code()
