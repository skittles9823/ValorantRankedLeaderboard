import urllib.request, json
import time

region = "AP"
URL = f"https://dgxfkpkb4zk5c.cloudfront.net/leaderboards/affinity/{region}/queue/competitive/act/97b6e739-44cc-ffa7-49ad-398ba502ceb0?startIndex=0&size=0"

with urllib.request.urlopen(f"{URL}") as url:
    data = json.loads(url.read().decode())

newSize = data['totalPlayers']
newIndex = 0
rank = 1
search = False
broken = False

def getLeaderboard(newIndex, newSize, rank, search, broken):
    while newIndex < newSize:
        newURL = f"https://dgxfkpkb4zk5c.cloudfront.net/leaderboards/affinity/{region}/queue/competitive/act/97b6e739-44cc-ffa7-49ad-398ba502ceb0?startIndex={newIndex}&size={newSize}"
        with urllib.request.urlopen(f"{newURL}") as url2:
            data = json.loads(url2.read().decode())
            try:
                for s in range(len(data['players'])):
                    if search:
                        if data['players'][s]['gameName'] == f"{search}":
                            print(str(data['players'][s]['leaderboardRank']) + ". " + str(data['players'][s]['gameName']) + "#" + str(data['players'][s]['tagLine']) + " | RR: " + str(data['players'][s]['rankedRating']) +
                                " | Wins: " + str(data['players'][s]['numberOfWins']))
                            broken = True
                            break
                    else:
                        print(str(data['players'][s]['leaderboardRank']) + ". " + str(data['players'][s]['gameName']) + "#" + str(data['players'][s]['tagLine']) + " | RR: " + str(data['players'][s]['rankedRating']) +
                            " | Wins: " + str(data['players'][s]['numberOfWins']))
                    rank += 1
            except KeyError:
                print(data)
                newIndex -= 10
                time.sleep(60)
            newIndex += 10
            if broken == True:
                break

getLeaderboard(newIndex, newSize, rank, search, broken)
