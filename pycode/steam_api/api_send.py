import requests


key = "C648B3B4DCF5146ABC9722EB910CD662"
target_url = "https://api.steampowered.com/"

params = {
    "key": key,
    "steamid": ""
}

# https://api.steampowered.com/<Интерфейс>/<Метод>/v<Версия>/?key=<Ваш_Ключ>&<Параметры>

response = requests.get("")
