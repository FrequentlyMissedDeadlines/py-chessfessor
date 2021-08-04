from typing import Any, List
import lichess.api as lichess_api
from lichess.format import PGN

class LichessExtractor:
    def extract_games(self, username: str) -> List[Any]:
        return list(lichess_api.user_games(username, max=2, clocks=True, evals=True, opening=True, format=PGN))
        