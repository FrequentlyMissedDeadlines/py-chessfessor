from mock import patch
from datetime import datetime
from types import SimpleNamespace

@patch('chessfessor.extractors.chessdotcom_extractor.chesscom')
def test_extract(mock):
    mock.get_player_profile.return_value = SimpleNamespace(**{'player': SimpleNamespace(**{'joined': datetime.timestamp(datetime.now())})})
    mock.get_player_games_by_month.return_value = SimpleNamespace(**{'json':{'games':[{'pgn':'game data'}]}})

    from chessfessor.extractors import ChessdotcomExtractor
    extractor = ChessdotcomExtractor()
    games = extractor.extract_games('mocked user')
    assert games == ['game data']