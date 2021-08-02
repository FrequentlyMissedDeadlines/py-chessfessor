#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(description='Extract your chess games data from https://lichess.org and https://chess.com.')
    parser.add_argument('username', help='The username of the player.', nargs=1)
    parser.add_argument('--include-casual', const=True, default=False, nargs='?', help='Include casual games. By default only rated games are downloaded.')
    parser.add_argument('--website', choices=['lichess', 'chessdotcom', 'both'], default='both', nargs='?', help='The website to extract the data from. Default value is "both".')
    
    args = parser.parse_args()
    print(args.include_casual)


if __name__ == '__main__':
	main()