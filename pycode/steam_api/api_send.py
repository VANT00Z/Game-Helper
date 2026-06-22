import requests


key = "C648B3B4DCF5146ABC9722EB910CD662"
target_url = "https://api.steampowered.com"
target_id = "76561199072544251"

params = {
    "key": key,
    "steamid": target_id,
    "format": "json"
}

# https://api.steampowered.com/<Интерфейс>/<Метод>/v<Версия>/?key=<Ваш_Ключ>&<Параметры>

# https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C648B3B4DCF5146ABC9722EB910CD662&steamids=76561197960435530

response = requests.get(
    f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=C648B3B4DCF5146ABC9722EB910CD662&steamids={target_id}")
if response.status_code == 200:
    try:
        data = response.json()
        print(data)
    except Exception as e:
        print("Error: ", e)
else:
    print(response.status_code)
    print(response.text)
