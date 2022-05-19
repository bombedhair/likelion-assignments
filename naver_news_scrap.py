import requests
from bs4 import BeautifulSoup


keyword = input("검색할 키워드를 입력해주세요: ")
page = int(input("검색할 페이지를 입력해주세요: "))
cursor = (page - 1) * 10 + 1

URL_SEARCH = f"https://search.naver.com/search.naver?where=news&query={keyword}&sort=1&start={cursor}"

response = requests.get(URL_SEARCH)
document = BeautifulSoup(response.text, 'html.parser')

articles = document.select("ul.list_news > li.bx > div > div > a")
print(f"네이버에 {keyword}를 검색했을 때의 뉴스 기사")
print(f"{page} 페이지의 {len(articles)}개의 기사가 검색 됨")

with open("articles.txt", "a+", encoding="UTF-8") as f:
    for i in range(0, len(articles)):
        text = f"{i+1:02}번째 기사 - {articles[i].get_text()}"
        print(text)
        f.write(text)
        f.write("\n")