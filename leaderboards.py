import requests
   
user_in = input("Enter a region code: ")
region = user_in.lower()
r = requests.get(f"https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}")
json_data = r.json()

def getUser(name):
    for s in range(len(json_data['data'])):
        if json_data['data'][s]['GameName'] == name:
            return (str(json_data['data'][s]['LeaderboardRank']) + ". " + json_data['data'][s]['GameName'] + "#" + json_data['data'][s]['TagLine'] + " | RR: " + str(json_data['data'][s]['RankedRating']) +" | Wins: " + str(json_data['data'][s]['NumberOfWins']))

print("")
print("If you want to see the whole leaderboard list -> l\n"
      "If you want to search a specific user -> u"
    )

check = input("[l/u]: ")
if check == "u":
    name = input("Enter user name without tag: ")
    print(getUser(name))

if check == "l":
    for s in range(len(json_data['data'])):
        print(str(json_data['data'][s]['LeaderboardRank']) + ". " + json_data['data'][s]['GameName'] + "#" + json_data['data'][s]['TagLine'] + " | RR: " + str(json_data['data'][s]['RankedRating']) +" | Wins: " + str(json_data['data'][s]['NumberOfWins']))