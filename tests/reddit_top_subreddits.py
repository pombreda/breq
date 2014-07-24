# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '..')

from breq.reddit import Reddit

headers = {'user-agent': 'redditor yaph'}
payload = {'limit': 10}
url = 'http://www.reddit.com/reddits/popular.json'

subreddits = []
pages = Reddit(url, headers=headers, payload=payload, max_requests=2)
for page in pages:
    for sr in page['data']['children']:
        subreddits.append(sr)

print(subreddits)