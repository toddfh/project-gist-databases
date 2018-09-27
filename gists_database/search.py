from .models import Gist
from pprint import pprint as pp


def search_gists(db_connection, **kwargs):
    if not kwargs:
        sql = 'SELECT * FROM gists'
        cursor = db_connection.execute(sql).fetchall()
        return cursor
    elif 'created_at' in kwargs:
        params = {
            'created_at': kwargs['created_at']
        }
        cursor = db_connection.execute("""
            SELECT *
            FROM gists
            WHERE datetime(created_at)==datetime(:created_at)
            """, params)

    elif 'github_id' in kwargs:
        params = {
            'github_id': kwargs['github_id']
        }
        cursor = db_connection.execute("""
            SELECT *
            FROM gists
            WHERE github_id=:github_id
            """, params)

    gists_table = []
    for row in cursor:
        gists_table.append(Gist(row))
    return gists_table
