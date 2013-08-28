.. _wikipedia:

Wikipedia
=========

Print the last 10 users that edited the Python language page.

::

    from breq.wikipedia import Wikipedia

    params = {
        'format': 'json',
        'action': 'query',
        'prop': 'revisions',
        'rvlimit': 1,
        'titles': 'Python_(programming_language)'
    }
    url = 'http://en.wikipedia.org/w/api.php'

    pages = Wikipedia(url, params, 10)
    for page in pages:
        rev_pages = page['query']['pages']
        for pageid, pagedata in rev_pages.items():
            print(pagedata['revisions'][0]['user'])


References
----------

* `Wikipedia API <https://www.mediawiki.org/wiki/API:Main_page>`_