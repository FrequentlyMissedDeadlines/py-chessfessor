from mock import patch

@patch('chessfessor.extractors.lichess_extractor.lichess_api')
def test_extract(mocker):
    mocker.user_games.return_value = iter(['mocked game'])
    from chessfessor.extractors import LichessExtractor
    extractor = LichessExtractor()
    games = extractor.extract_games('mocked user')
    assert games == ['mocked game']