import requests
import sqlite3
from pprint import pprint as pp
from requests import exceptions


def import_gists_to_database(db, username, commit=True):
    gists_url = 'https://api.github.com/users/{}/gists'.format(username)

    gists = requests.get(gists_url)
    if gists.status_code == 404:
        raise exceptions.HTTPError
    gists_json = gists.json()

    for gist in gists_json:
        gist_fields = {
            'github_id': gist['id'],
            'html_url': gist['html_url'],
            'git_pull_url': gist['git_pull_url'],
            'git_push_url': gist['git_push_url'],
            'commits_url': gist['commits_url'],
            'forks_url': gist['forks_url'],
            'public': gist['public'],
            'created_at': gist['created_at'],
            'updated_at': gist['updated_at'],
            'comments': gist['comments'],
            'comments_url': gist['comments_url']
        }

        sql = """INSERT INTO gists (github_id, html_url, git_pull_url,
                                    git_push_url, commits_url, forks_url,
                                    public, created_at, updated_at, comments,
                                    comments_url) VALUES (:github_id, :html_url,
                                    :git_pull_url, :git_push_url,:commits_url,
                                    :forks_url, :public, :created_at,
                                    :updated_at, :comments, :comments_url)"""

        db.execute(sql, gist_fields)
