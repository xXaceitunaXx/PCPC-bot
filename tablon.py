import requests


class Tablon:

    def __init__(self, url: str):
        self.__url = url

    def extract_table(self, name: str):
        leaderboard_url = f"{self.__url}/leaderboards"
        leaderboard_content = requests.get(leaderboard_url)

        # Esto lo terminaré otro día XD

        if not name in leaderboard_content:
            raise ValueError(f"No table for that name: {name}")
