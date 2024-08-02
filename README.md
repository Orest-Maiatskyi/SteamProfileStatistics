# SteamProfileStatistics
Web app created with Flask that uses steam api for getting profile statistics.

## About
![image](https://github.com/user-attachments/assets/9b567aac-7b54-4711-8ce4-e5b90d34070b)
Statistics include:
1. Total account games count (games that were hidden from view are not counted)
2. Total achievements number
3. Total games hours played
4. Five most played games
5. General statistics for all games (At the moment it only shows the number of hours played in a specific game)

## Future Releases
1. At the moment, switching tabs with games does not work.
2. General statistics will include all achievements for a game and more complex statistics with graphs.

## How to run
1. Create venv with 'python -m venv venv'
2. Install all dependencies from 'requirements.txt'
3. Update 'config.py', set 'STEAM_API_KEY'.
4. start 'entry.py'
