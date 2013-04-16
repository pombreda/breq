# coding: utf-8
from breq.github import Github
url = 'https://api.github.com/users/yaph/repos'

repo_pages = Github(url, {}, 2)
for repos in repo_pages:
    for repo in repos:
        print repo['html_url']