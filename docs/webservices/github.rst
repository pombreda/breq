.. _github:

GitHub
======

Get a list of all GitHub repositories for a user.

::

    from breq.github import Github
    url = 'https://api.github.com/users/yaph/repos'

    repos = []
    pages = Github(url, {}, 2)
    for page in pages:
        for repo in page:
            repos.append(repo)


References
----------

* `GitHub API Documentation <http://developer.github.com/>`_