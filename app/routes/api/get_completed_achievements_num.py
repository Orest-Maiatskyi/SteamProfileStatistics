from threading import Thread

from flask import abort

from app import app, current_config
from app.steam_web_api import *


@app.route('/api/get_completed_achievements_num/<user_id>', methods=['GET'])
def get_completed_achievements_num(user_id):
    key = current_config.STEAM_API_KEY
    player = SteamWebApi.get_player_summaries_v0002(key, user_id).json()
    if len(player['response']['players']) == 0:
        abort(404)

    games = SteamWebApi.get_owned_games_v0001(key, user_id, True, True).json()

    class AchievementsNum:
        def __init__(self):
            self.num = 0

    achievements_num = AchievementsNum()

    def set_achievements_num_for_a_games(key, user_id, games, achievements_num):
        for game in games:
            response = SteamWebApi.get_player_achievements_v0001(key, user_id, game['appid']).json()
            if 'achievements' in response['playerstats']:
                for a in response['playerstats']['achievements']:
                    if a['achieved'] == 1:
                        achievements_num.num += 1

    threads = []
    counter = 0
    current_thread_games = []
    for game in games['response']['games']:
        if counter == 20:
            threads.append(
                Thread(target=set_achievements_num_for_a_games,
                       args=[key, user_id, current_thread_games, achievements_num],
                       daemon=True))
            counter = 1
            current_thread_games = []
        current_thread_games.append(game)
        counter += 1

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    return {"num": achievements_num.num}
