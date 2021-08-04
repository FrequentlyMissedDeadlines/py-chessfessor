from typing import Any, List
from datetime import datetime, date
from dateutil import rrule
import chessdotcom as chesscom

class ChessdotcomExtractor:
    def extract_games(self, username: str) -> List[Any]:
        profile = chesscom.get_player_profile(username)
        start_date = datetime.fromtimestamp(profile.player.joined)
        start_date = date(start_date.year, start_date.month, 1)
        now = datetime.now()
        now = date(now.year, now.month, 1)
        print('start_date', start_date, profile)
        games = []
        for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=now):
            response = chesscom.get_player_games_by_month(username=username, month=dt.month, year=dt.year)
            if response.json['games']:
                games.extend(list(map(lambda x: x['pgn'], response.json['games'])))
        return games
