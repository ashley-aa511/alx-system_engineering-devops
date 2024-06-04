#!/usr/bin/python3

"""
This module provides functionality to query the Reddit API and print the
titles of the first 10 hot posts for a given subreddit.

Functions:
    top_ten(subreddit): Prints the titles of the first 10 hot posts for a 
                        specified subreddit. Prints None if the subreddit 
                        is invalid or an error occurs.
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API to print the titles of the first 10 hot posts for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'custom_user_agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except (KeyError, ValueError):
        print(None)

# Example usage:
# if __name__ == "__main__":
#     subreddit_name = "python"
#     top_ten(subreddit_name)
