import requests
import sys

user_in = input("Enter a region code (eu, na, kr, ap): ")
region = user_in.lower()
r = requests.get(f"https://api.henrikdev.xyz/valorant/v1/leaderboard/{region}")
json_data = r.json()

try:
    if json_data['message']:
        print(json_data['message'])
        exit()
    else:
        pass
except KeyError:
    pass

def getUser(name):
    users = ""
    for s in range(len(json_data['data'])):
        if name.lower() in str(json_data['data'][s]['gameName'] + "#" + json_data['data'][s]['tagLine']).lower():
            users += str(json_data['data'][s]['leaderboardRank']) + ". " + json_data['data'][s]['gameName'] + "#" + json_data['data'][s]['tagLine'] + " | RR: " + str(json_data['data'][s]['rankedRating']) +" | Wins: " + str(json_data['data'][s]['numberOfWins']) + "\n"
    return users.rstrip()


def getUserOfRank(rank):
    for s in range(len(json_data['data'])):
        if str(rank) in str(json_data['data'][s]['leaderboardRank']):
            if not json_data['data'][s]['gameName'] and not json_data['data'][s]['tagLine']:
                return (str(json_data['data'][s]['leaderboardRank']) + ". " + "Secret Agent" + " | RR: " + str(json_data['data'][s]['rankedRating']) +" | Wins: " + str(json_data['data'][s]['numberOfWins']))
            else:
                return (str(json_data['data'][s]['leaderboardRank']) + ". " + json_data['data'][s]['gameName'] + "#" + json_data['data'][s]['tagLine'] + " | RR: " + str(json_data['data'][s]['rankedRating']) +" | Wins: " + str(json_data['data'][s]['numberOfWins']))

def getTopX(topx):
    text = ""
    for s in range(topx):
        if not json_data['data'][s]['gameName'] and not json_data['data'][s]['tagLine']:
            text += str(json_data['data'][s]['leaderboardRank']) + ". " + "Secret Agent" + " | RR: " + str(json_data['data'][s]['rankedRating']) +" | Wins: " + str(json_data['data'][s]['numberOfWins']) + "\n"
        else:
            text += str(json_data['data'][s]['leaderboardRank']) + ". " + json_data['data'][s]['gameName'] + "#" + json_data['data'][s]['tagLine'] + " | RR: " + str(json_data['data'][s]['rankedRating']) +" | Wins: " + str(json_data['data'][s]['numberOfWins']) + "\n"
    return text[:-1]


def listLeaderboard():
    for s in range(len(json_data['data'])):
        if not json_data['data'][s]['gameName'] and not json_data['data'][s]['tagLine']:
            print(str(json_data['data'][s]['leaderboardRank']) + ". " + "Secret Agent" + " | RR: " + str(json_data['data'][s]['rankedRating']) +" | Wins: " + str(json_data['data'][s]['numberOfWins']))
        else:
            print(str(json_data['data'][s]['leaderboardRank']) + ". " + json_data['data'][s]['gameName'] + "#" + json_data['data'][s]['tagLine'] + " | RR: " + str(json_data['data'][s]['rankedRating']) +" | Wins: " + str(json_data['data'][s]['numberOfWins']))

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
