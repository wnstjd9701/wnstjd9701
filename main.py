import feedparser
import time
URL="https://dev-wnstjd.tistory.com/rss" # URL = "내블로그 주소/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 2

# 기본적으로 바뀌지 않을 Markdown text 입력
markdown_text = """
<div class='tech-stack' align='left'>
  <h2> 🛠 TECH STACK </h2>
  <h4> 📚 Language : &nbsp
  <img src="https://img.shields.io/badge/python-3776AB?style=flat&logo=python&logoColor=white">  
  <img alt="Java" src ="https://img.shields.io/badge/Java-007396?&style=flat&logo=Java&logoColor=white"/>
  <img src="https://img.shields.io/badge/javascript-F7DF1E?style=flat&logo=javascript&logoColor=black">&nbsp 
  <h4>
  
  <h4> 🟨 Front-End : &nbsp
  <img src="https://img.shields.io/badge/html5-E34F26?style=flat&logo=html5&logoColor=white"> 
  <img src="https://img.shields.io/badge/css3-1572B6?style=flat&logo=css3&logoColor=white"> 
  <h4>

  <h4> 🟩 Back-End : &nbsp
  <img src="https://img.shields.io/badge/node.js-339933?style=flat&logo=Node.js&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/mysql-4479A1?style=flat&logo=mysql&logoColor=white">&nbsp
  <h4>

  <h4> 💻 Infra : &nbsp
  <img src="https://img.shields.io/badge/AWS EC2-FF9900?style=flat&logo=amazonec2&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/AWS RDS-527FFF?style=flat&logo=amazonrds&logoColor=white">&nbsp
  <img src="https://img.shields.io/badge/github-181717?style=flat&logo=github&logoColor=white">
  <h4>
</div>

<div class='blog' align='center'>
<h2 class='post' align='left'> ✅ Posting<h2>

[![Tistory's Badge](https://github-readme-tistory-card.vercel.app/api/badge?name=준성`s블로그&theme=kakao)](https://dev-wnstjd.tistory.com)
<br>
"""

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_num = feed['links']
        feed_number = feed_num[0]['href'].split('/')[-1] # feed number
        # feed_date = feed['published_parsed']
        # markdown_text += f" - [[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday}] - {feed['title']}]({feed['link']})\n"
        markdown_text += f"[![Tistory's Card](https://github-readme-tistory-card.vercel.app/api?name=dev-wnstjd.tistory.com&postId={feed_number}&theme=tistory)](https://dev-wnstjd.tistory.com/{feed_number})"
markdown_text +=  """
</div>
</div>
"""
f = open("README.md", mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()