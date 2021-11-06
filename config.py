HEADER_URL = "https://cdn.cloudflare.steamstatic.com/steam/apps/{}/header.jpg"
STEAM_ID_URL = "https://api.steampowered.com/ISteamUser/ResolveVanityURL/v1/?key={}&vanityurl={}"
OWNED_GAMES_URL = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={}&steamid={}&include_appinfo=true&include_played_free_games=true&include_free_sub=true"
STEAMSPY_INFO_URL = "https://steamspy.com/api.php?request=appdetails&appid={}"
STEAM_INFO_URL = "https://store.steampowered.com/api/appdetails/?appids={}"
STEAM_APP_LINK_URL = "https://store.steampowered.com/app/{}"
EXCEL_MAPPER = {'steam_appid': 1,
                'app_link': 2,
                'name': 3,
                'total_reviews': 4,
                'positive': 5,
                'negative': 6,
                'score': 7,
                'developers': 8,
                'price_overview': 9,
                'release_date': 10,
                'tags': 11,
                'username': 12}

REQUEST_DELAY = 60
REQUEST_LIMIT = 70
DATA_PATH = "data.xlsx"
IMG_PATH = "img/"
