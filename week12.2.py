import json
import requests

mario = {"name": "Mario", "age": 40, "occupation": "Plumber"}

mario["name"] = "Mario Mario"

json.dump(mario, open("mario.json", "w"), indent=4)

# print("Data saved to mario.json")

new_mario = json.load(open("/workspaces/DATA_3500_sandbox/mario.json"))

# print(new_mario)

url = "https://v2.jokeapi.dev/joke/programming"
# print(request.text)

while True:
    request = requests.get(url)
    keep_going = input("Do you want to see a programming joke? (yes/no): ")
    if keep_going.lower() != "yes":
        print("Okay, no more jokes.")
        break   
    request_dict = json.loads(request.text)
    if request_dict["type"] == "single":
        print(request_dict["joke"])
    else:
        print(request_dict["setup"], "\n", request_dict["delivery"])
