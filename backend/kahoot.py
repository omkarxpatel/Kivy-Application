from kivymd.toast import toast
import requests

def kahoot():
    

    game_pin = "5500119"
    username = "Player1"

    payload = {"gameid": game_pin, "username": username}
    response = requests.post("https://kahoot.it/rest/authenticate", json=payload)

    # two_factor_auth = response.json()["twoFactorAuth"]

    # payload = {"gameid": game_pin, "username": username, "twoFactorAuth": two_factor_auth}
    # response = requests.put("https://kahoot.it/rest/authenticate", json=payload)

    # kahoot_session_token = response.json()["kahootSessionToken"]

    # join_game_endpoint = f"https://kahoot.it/rest/games/{game_pin}/join"
    # headers = {"Authorization": kahoot_session_token}
    # response = requests.post(join_game_endpoint, headers=headers)

