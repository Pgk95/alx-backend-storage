#!/usr/bin/env python3
"""Redis module"""

import redis
import requests
import time

r = redis.Redis(host='localhost', port=6379, db=0)


def get_page(url: str) -> str:
    """get page"""
    count_key = f'count:{url}'
    cached_html = r.get(url)

    if cached_html is None:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.text
            r.setex(url, 10, html_content)
        else:
            return f"Failed to fetch URL: {url}"
    else:
        r.incr(count_key)

    access_count = r.get(count_key) if r.exists(count_key) else "0"

    return f"Access count: {access_count}\n\n{cached_html}"


if __name__ == "__main__":
    test_url = 'http://slowwly.robertomurray.co.uk'
    page_content = get_page(test_url)
    print(page_content)
