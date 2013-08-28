# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '..')

from breq.reddit import Reddit

headers = {'user-agent': 'redditor yaph'}
url = 'http://www.reddit.com/reddits/popular.json'

subreddits = Reddit(url, headers=headers, max_requests=2)
for page in subreddits:
    for sr in page['data']['children']:
        print(sr['data']['display_name'])