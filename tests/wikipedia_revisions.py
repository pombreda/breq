# coding: utf-8
# Print the last 10 users that edited the Python language page.
import sys
sys.path.insert(0, '..')

from breq.wikipedia import Wikipedia

params = {
    'format': 'json',
    'action': 'query',
    'prop': 'revisions',
    'rvlimit': 1,
    'titles': 'Python_(programming_language)'
}
url = 'http://en.wikipedia.org/w/api.php'

pages = Wikipedia(url, params, max_requests=2)
for page in pages:
    rev_pages = page['query']['pages']
    for pageid, pagedata in rev_pages.items():
        print(pagedata['revisions'][0]['user'])