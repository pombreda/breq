# coding: utf-8
import sys
sys.path.insert(0, '..')

from breq.github import Github
url = 'https://api.github.com/users/yaph/repos'

repos = []
pages = Github(url, {}, 2)
for page in pages:
    for repo in page:
        repos.append(repo)