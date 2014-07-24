# -*- coding: utf-8 -*-
from fabric.api import local, lcd


def build_docs():
    local('python setup.py build_sphinx')


def docs():
    build_docs()
    local('python setup.py upload_sphinx')


def release():
    local('python setup.py sdist upload')


def tests():
    with lcd('tests'):
        local('python ./github_repos.py')
        local('python ./reddit_top_subreddits.py')
        local('python ./wikipedia_revisions.py')