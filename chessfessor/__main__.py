#!/usr/bin/env python

import argparse
from chessfessor.extractors import *

def main():
    parser = argparse.ArgumentParser(description='Extract your chess games data from https://lichess.org and https://chess.com.')
    parser.add_argument('username', help='The username of the player.', nargs=1)
    parser.add_argument('--include-casual', const=True, default=False, nargs='?', help='Include casual games. By default only rated games are downloaded.')
    parser.add_argument('-w', '--website', choices=['lichess', 'chessdotcom', 'both'], default='both', nargs='?', help='The website to extract the data from. Default value is "both".')
    
    args = parser.parse_args()
    games = []
    if args.website == 'both' or args.website == 'lichess':
        extractor = LichessExtractor()
        games.extend(extractor.extract_games(args.username[0]))
    if args.website == 'both' or args.website == 'chessdotcom':
        extractor = ChessdotcomExtractor()
        games.extend(extractor.extract_games(args.username[0]))

    f = open(args.username[0], "w")
    f.write('\n'.join(games))
    f.close()

if __name__ == '__main__':
	main()