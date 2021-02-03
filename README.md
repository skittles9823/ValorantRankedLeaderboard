# ValorantRankedLeaderboard
### A simple python script which allows you to search and list the full Valorant leaderboards in any region.


## Usage Syntax
```
List all users in the leaderboard:
python3 leaderboards.py --list

python3 leaderboards.py --list
Enter a region code (eu, na, kr, ap): ap
1. PPK#2626 | RR: 816 | Wins: 49
2. KX MidnighT#dad | RR: 778 | Wins: 59
3. pl1xx#668 | RR: 721 | Wins: 57
4. EXO Crunchy#sayuu | RR: 684 | Wins: 88
5. dizzyLife#OCE | RR: 666 | Wins: 51
6. LFS W1nner#LFS | RR: 665 | Wins: 66
7. kZm#0422 | RR: 635 | Wins: 82
8. NG PTC#Odin | RR: 617 | Wins: 66
9. X10 foxz#LUL | RR: 615 | Wins: 73
10. Maple#7635 | RR: 610 | Wins: 73
...
```
```
Search for specific users in the leaderboard:
python3 leaderboards.py --search username

python3 leaderboards.py --search ppk
Enter a region code (eu, na, kr, ap): ap
1. PPK#2626 | RR: 816 | Wins: 49
```
```
Search for a specific rank place in the leaderbord:
python3 leaderboards.py --rank number

python3 leaderboards.py --rank 500
Enter a region code (eu, na, kr, ap): ap
There are currently 4852 users in the Immortal+ leaderboards for ap
500. DxE Yvesaur#Erica | RR: 261 | Wins: 58
```
```
List the top x players in the leaderboard:
python3 leaderboards.py --top number

python3 leaderboards.py --top 10
Enter a region code (eu, na, kr, ap): ap
There are currently 5934 users in the Immortal+ leaderboards for ap
1. EXO Crunchy#sayuu | RR: 780 | Wins: 97
2. EDG YeeeZ#EDG | RR: 776 | Wins: 71
3. pl1xx#668 | RR: 748 | Wins: 60
4. dizzyLife#OCE | RR: 720 | Wins: 67
5. NG PTC#Odin | RR: 702 | Wins: 92
6. NG JohnOlsen#black | RR: 691 | Wins: 98
7. jmz#OCE | RR: 680 | Wins: 125
8. SAIKO73#Py73 | RR: 664 | Wins: 61
9. kZm#0422 | RR: 656 | Wins: 83
10. IRIS Singurality#Levi | RR: 645 | Wins: 51
```
```
Run the script normally and follow the prompts:
python3 leaderboards.py

python3 leaderboards.py
Enter a region code (eu, na, kr, ap): ap

If you want to see the whole leaderboard list -> l
If you want to search a specific user -> u
If you want to get the info for a specific rank number -> n
If you want to list the top x players -> t
[l/u/n/t]: u
Enter user name without tag: ppk
1. PPK#2626 | RR: 816 | Wins: 49
```