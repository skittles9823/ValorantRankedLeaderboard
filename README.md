# ValorantRankedLeaderboard
### A simple python script which allows you to search and list the full Valorant leaderboards in any region.


## Usage Syntax
```
List all users in the leaderboard:
python3 leaderboards.py --list

C:\Users\Skittles\Desktop> python3 leaderboards.py --list
Enter a region code (eu, na, ko, ap): ap
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

C:\Users\Skittles\Desktop> python3 leaderboards.py --search ppk
Enter a region code (eu, na, ko, ap): ap
1. PPK#2626 | RR: 816 | Wins: 49
```
```
Run the script normally and follow the prompts:
python3 leaderboards.py

C:\Users\Skittles\Desktop> python3 leaderboards.py
Enter a region code (eu, na, ko, ap): ap

If you want to see the whole leaderboard list -> l
If you want to search a specific user -> u
[l/u]: u
Enter user name without tag: ppk
1. PPK#2626 | RR: 816 | Wins: 49
```