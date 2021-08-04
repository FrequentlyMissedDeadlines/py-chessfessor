from mock import patch


@patch('lichess_extractor.lichess_api')
def test_extract(mocker):
    mocker.user_games.return_value = iter(['mocked game'])
    from lichess_extractor import LichessExtractor
    extractor = LichessExtractor()
    games = extractor.extract_games('mocked user')
    assert games == ['mocked game']