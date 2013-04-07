# coding: utf-8
from breq.wikipedia import Wikipedia

params = {
    'format': 'json',
    'action': 'query',
    'prop': 'revisions',
    'rvlimit': 1,
    'titles': 'Python_(programming_language)'
}
url = 'http://en.wikipedia.org/w/api.php'

# fetch a maximum of 2 pages
revisions = Wikipedia(url, params, 2)
for revision in revisions:
    # do more sensible stuff here
    pages = revision['query']['pages']
    for pageid, pagedata in pages.items():
        print(pagedata['revisions'][0]['user'])