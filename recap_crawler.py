import requests


def get_recap(game_id):
    url_ = None
    r = requests.get(
        url="https://content-api-prod.nba.com/public/1/content/video/",
        params={"games": game_id}
    )
    data = r.json()
    recap = [i for i in data['results']['items'] if i['taxonomy']['categories'].get('game-recap')]
    if recap:
        url_ = recap[0].get('endeavorVideo')
    return url_


if __name__ == '__main__':
    print(get_recap('0042000312'))