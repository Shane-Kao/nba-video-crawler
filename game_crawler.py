import requests


def get_games():
    r = requests.get(
        url="https://nba-prod-us-east-1-mediaops-stats.s3.amazonaws.com/"
            "NBA/liveData/scoreboard/todaysScoreboard_00.json"
    )
    data = r.json()
    game_date = data['scoreboard']['gameDate']
    games = [dict(gameId=i['gameId'], gameCode=i['gameCode']) for i in data['scoreboard']['games']]
    return game_date, games