#!/usr.bin/python3

"""
This module provides functionality to query the Reddit API and retrieve
all hot article titles for a given subreddit using recursion.

Functions:
    recurse(subreddit, hot_list=[]): Returns a list of titles of all hot articles 
                                     for a specified subreddit. Returns None if 
                                     the subreddit is invalid or no results are found.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to get titles of all hot articles for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to accumulate the titles of hot articles.
        after (str): The parameter for pagination.

    Returns:
        list: A list of titles of all hot articles for the subreddit. Returns None if
              the subreddit is invalid or no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'custom_user_agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        
        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except (KeyError, ValueError):
        return None

# Example usage:
# if __name__ == "__main__":
#     subreddit_name = "python"
#     titles = recurse(subreddit_name)
#     if titles is not None:
#         print(f"Titles of all hot articles in r/{subreddit_name}:")
#         for title in titles:
#             print(title)
#     else:
#         print("No results found or invalid subreddit.")
