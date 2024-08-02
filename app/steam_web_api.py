import enum
import json
from typing import Callable, Any, Dict, Tuple, Type, Optional, Union, List

import requests


class SteamWebApiResponseFormats(enum.Enum):
    JSON = 'json'
    XML = 'xml'
    VDF = 'vdf'


class SteamWebApiRelationshipFilters(enum.Enum):
    ALL = 'all'
    FRIEND = 'friend'


class SteamWebApiSupportedLanguages:
    ARABIC = 'arabic'
    BULGARIAN = 'bulgarian'
    SCHINESE = 'schinese'
    TCHINESE = 'tchinese'
    CZECH = 'czech'
    DANISH = 'danish'
    DUTCH = 'dutch'
    ENGLISH = 'english'
    FINNISH = 'finnish'
    FRENCH = 'french'
    GERMAN = 'german'
    GREEK = 'greek'
    HUNGARIAN = 'hungarian'
    INDONESIAN = 'indonesian'
    ITALIAN = 'italian'
    JAPANESE = 'japanese'
    KOREANA = 'koreana'
    NORWEGIAN = 'norwegian'
    POLISH = 'polish'
    PORTUGUESE = 'portuguese'
    BRAZILIAN = 'brazilian'
    ROMANIAN = 'romanian'
    RUSSIAN = 'russian'
    SPANISH = 'spanish'
    LATAM = 'latam'
    SWEDISH = 'swedish'
    THAI = 'thai'
    TURKISH = 'turkish'
    UKRAINIAN = 'ukrainian'
    VIETNAMESE = 'vietnamese'


def kwargs_to_params(kwargs: Dict[str, Any]) -> Dict[str, str]:
    return {k: (str(v.value) if isinstance(v, enum.Enum) else str(v)) for k, v in kwargs.items() if v is not None}


def kwargs_to_json(kwargs: Dict[str, Any]):
    return json.dumps(
        {k: (v.value if isinstance(v, enum.Enum) else v) for k, v in kwargs.items() if v is not None and k != 'format'},
        indent=0)


def steam_web_api_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


class SteamWebApiMeta(type):

    def __new__(mcs: Type['SteamWebApiMeta'], name: str, bases: Tuple[type, ...], dct: Dict[str, Any]) -> Any:
        for k, v in dct.items():
            if isinstance(v, staticmethod):
                dct[k] = staticmethod(steam_web_api_decorator(v.__func__))
        return super().__new__(mcs, name, bases, dct)


class SteamWebApi(metaclass=SteamWebApiMeta):

    @staticmethod
    def get_news_for_app_v0002(
            app_id: Union[int, str],
            count: Optional[Union[int, str]] = None,
            maxlength: Optional[Union[int, str]] = None,
            format: Optional[SteamWebApiResponseFormats] = None
    ) -> requests.Response:
        return requests.get('http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/',
                            params={
                                'appid': str(app_id),
                                **kwargs_to_params(locals())
                            })

    @staticmethod
    def get_global_achievement_percentages_for_app_v0002(
            gameid: Union[int, str],
            format: Optional[SteamWebApiResponseFormats] = None
    ) -> requests.Response:
        return requests.get('http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/',
                            params={
                                'gameid': str(gameid),
                                **kwargs_to_params(locals())
                            })

    @staticmethod
    def get_player_summaries_v0002(
            key: str,
            steamids: Union[str, List[Union[int, str]]],
            format: Optional[SteamWebApiResponseFormats] = None
    ) -> requests.Response:
        return requests.get('http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/',
                            params={
                                'key': key,
                                'steamids': steamids if isinstance(steamids, str) else ','.join(steamids),
                                **kwargs_to_params(locals())
                            })

    @staticmethod
    def get_friend_list_v0001(
            key: str,
            steamid: Union[int, str],
            relationship: Optional[SteamWebApiRelationshipFilters] = None,
            format: Optional[SteamWebApiResponseFormats] = None
    ) -> requests.Response:
        return requests.get('http://api.steampowered.com/ISteamUser/GetFriendList/v0001/',
                            params={
                                'key': key,
                                'steamid': str(steamid),
                                **kwargs_to_params(locals())
                            })

    @staticmethod
    def get_player_achievements_v0001(
            key: str,
            steamid: Union[int, str],
            appid: Union[int, str],
            l: Optional[SteamWebApiSupportedLanguages] = None,
            format: Optional[SteamWebApiResponseFormats] = None
    ) -> requests.Response:
        return requests.get('http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/',
                            params={
                                'key': key,
                                'steamid': str(steamid),
                                'appid': str(appid),
                                **kwargs_to_params(locals())
                            })

    @staticmethod
    def get_user_stats_for_game_v0002(
            key: str,
            steamid: Union[int, str],
            appid: Union[int, str],
            l: Optional[SteamWebApiSupportedLanguages] = None,
            format: Optional[SteamWebApiResponseFormats] = None
    ) -> requests.Response:
        return requests.get('http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/',
                            params={
                                'key': key,
                                'steamid': str(steamid),
                                'appid': str(appid),
                                **kwargs_to_params(locals())
                            })

    @staticmethod
    def get_owned_games_v0001(
            key: str,
            steamid: Union[int, str],
            include_appinfo: Optional[Union[int, str, bool]] = None,
            include_played_free_games: Optional[Union[int, str, bool]] = None,
            format: Optional[SteamWebApiResponseFormats] = None,
            appids_filter: Optional[List[Union[int, str]]] = None
    ) -> requests.Response:
        return requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/',
                            params={
                                'key': key,
                                'format': format.value if isinstance(format, SteamWebApiResponseFormats) else 'json',
                                'input_json': kwargs_to_json(locals())
                            })

    @staticmethod
    def get_recently_played_games_v0001(
            key: str,
            steamid: Union[int, str],
            count: Optional[Union[int, str]] = None,
            format: Optional[SteamWebApiResponseFormats] = None
    ) -> requests.Response:
        return requests.get('http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/',
                            params={
                                'key': key,
                                'steamid': str(steamid),
                                **kwargs_to_params(locals())
                            })


if __name__ == '__main__':
    pass
