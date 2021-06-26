import requests


def get_recap(game_id):
    url_ = None
    r = requests.get(
        url="https://content-api-prod.nba.com/public/1/content/video/",
        params={"games": game_id}
    )
    data = r.json()
    recap = [i for i in data['results']['items'] if i['taxonomy'].get('categories', {}).get('game-recap')]
    if recap:
        url_ = recap[0].get('endeavorVideo')
    return url_


if __name__ == '__main__':
    from game_crawler import get_games
    game_date, games = get_games()
    print(game_date)

    for i in games:
        m3u8_url = get_recap(i['gameId'])
        game_code = i['gameCode']
        print(game_code, m3u8_url)

