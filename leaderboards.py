import requests
import sys

user_in = input("Enter a region code (eu, na, kr, ap): ")
region = user_in.lower()
r = requests.get(f"https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}")
json_data = r.json()


print("There are currently " + str(json_data['data'][-2]['LeaderboardRank']) + f" users in the Immortal+ leaderboards for {region}")


def getUser(name):
    for s in range(len(json_data['data'])):
        if name.lower() in json_data['data'][s]['GameName'].lower():
            return (str(json_data['data'][s]['LeaderboardRank']) + ". " + json_data['data'][s]['GameName'] + "#" + json_data['data'][s]['TagLine'] + " | RR: " + str(json_data['data'][s]['RankedRating']) +" | Wins: " + str(json_data['data'][s]['NumberOfWins']))


def getUserOfRank(rank):
    for s in range(len(json_data['data'])):
        if str(rank) in str(json_data['data'][s]['LeaderboardRank']):
            return (str(json_data['data'][s]['LeaderboardRank']) + ". " + json_data['data'][s]['GameName'] + "#" + json_data['data'][s]['TagLine'] + " | RR: " + str(json_data['data'][s]['RankedRating']) +" | Wins: " + str(json_data['data'][s]['NumberOfWins']))


def getTopX(topx):
    text = ""
    for s in range(topx):
        text += str(json_data['data'][s]['LeaderboardRank']) + ". " + json_data['data'][s]['GameName'] + "#" + json_data['data'][s]['TagLine'] + " | RR: " + str(json_data['data'][s]['RankedRating']) +" | Wins: " + str(json_data['data'][s]['NumberOfWins']) + "\n"
    return text[:-1]


def listLeaderboard():
    for s in range(len(json_data['data'])):
        print(str(json_data['data'][s]['LeaderboardRank']) + ". " + json_data['data'][s]['GameName'] + "#" + json_data['data'][s]['TagLine'] + " | RR: " + str(json_data['data'][s]['RankedRating']) +" | Wins: " + str(json_data['data'][s]['NumberOfWins']))
    

def noCLI():
    print("")
    print("If you want to see the whole leaderboard list -> l\n"
          "If you want to search a specific user -> u\n"
          "If you want to get the info for a specific rank number -> n\n"
          "If you want to list the top x players -> t"
        )

    check = input("[l/u/n/t]: ").lower()
    if check == "u":
        name = input("Enter user name without tag: ")
        print(getUser(name))
    
    if check == "n":
        rank = input("Enter rank number (eg. 500): ")
        print(getUserOfRank(rank))

    if check == "t":
        topx = int(input("Enter how many players to list number (eg. 10): "))
        print(getTopX(topx))

    if check == "l":
        listLeaderboard()

if len(sys.argv) > 1:
    if sys.argv[1] == "--list":
        listLeaderboard()

    if sys.argv[1] == "--search":
        name = sys.argv[2]
        print(getUser(name))

    if sys.argv[1] == "--rank":
        rank = sys.argv[2]
        print(getUserOfRank(rank))
    
    if sys.argv[1] == "--top":
        topx = int(sys.argv[2])
        print(getTopX(topx))

else:
    noCLI()
