import feedparser
import time
URL="https://dev-wnstjd.tistory.com/rss" # URL = "내블로그 주소/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
## ✅ Latest Tistory Posting
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"
        print(markdown_text)
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()