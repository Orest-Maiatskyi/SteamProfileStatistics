import json

from flask import render_template, abort

from app import app, current_config
from app.steam_web_api import *


@app.route('/statistics/<user_id>', methods=['GET'])
def statistics(user_id):
    key = current_config.STEAM_API_KEY
    player = SteamWebApi.get_player_summaries_v0002(key, user_id).json()

    if len(player['response']['players']) == 0:
        abort(404)

    games = SteamWebApi.get_owned_games_v0001(key, user_id, True, True).json()
    play_time_all = 0

    for game in games['response']['games']:
        play_time_all += int(game['playtime_forever'])

    play_time_all = play_time_all // 60

    return render_template('statistics.html',
                           account_name=player['response']['players'][0]['personaname'],
                           play_time_all=play_time_all,
                           games_num=games['response']['game_count'],
                           most_played_games=sorted(games['response']['games'], key=lambda d: d['playtime_forever'])[-5:],
                           games=json.dumps(games['response']['games']))
