.. _reddit:

Reddit
======

Get a list of the top 1000 subreddits by popularity.

::

    from breq.reddit import Reddit

    headers = {'user-agent': 'redditor username'}
    payload = {'limit': 100}
    url = 'http://www.reddit.com/reddits/popular.json'

    subreddits = []
    pages = Reddit(url, headers=headers, payload=payload, max_requests=10)
    for page in pages:
        for sr in page['data']['children']:
            subreddits.append(sr)


References
----------

* `Reddit API Documentation <http://www.reddit.com/dev/api>`_
