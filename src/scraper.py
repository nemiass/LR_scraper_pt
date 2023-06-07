import requests
from bs4 import BeautifulSoup

class NewsModel:
    def __init__(self) -> None:    
        self.title: str
        self.summary: str
        self.publication_date: str
        self.author: str
        self.link: str 
        self.category: str

    def __str__(self) -> str:
        return f"{self.title} - {self.summary}"

class LaRepublicaScraper:
    def __init__(self, target_url: str, base_url, limit: int) -> None:
        self.url = target_url
        self.base_url = base_url
        self.limit = limit
        self.data = []

        # class to get the links of the first 10 news
        self.news_links_class = "extend-link"
        # class to get time of publication
        self.time_class = "TitleSection_main__date__L_7Cf"
        # class to get author of publication
        self.author_class = "Author_author__redSocial_link__ZcaC8"
        # class to get category title of publication
        self.category_class = "TitleSection_titleSection__main__UjavR"

    def start_scraper(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
        response = requests.get(self.url, headers=headers)

        if response.status_code != 200:
            return
        
        soup = BeautifulSoup(response.text, "html.parser")

        # find the links of the first 10 news
        links = soup.find_all("a", class_=self.news_links_class, limit=self.limit)

        for l in links:
            href = l.get("href")
            new_url = f"{self.base_url}{href}"
            response = requests.get(new_url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, "html.parser")
                news = NewsModel()
                news.title = soup.h1.text
                news.summary = soup.h2.text 
                news.publication_date = soup.find("time", class_=self.time_class).get("datetime")
                news.author = soup.find("a", class_=self.author_class).text 
                news.category = soup.find("span", class_=self.category_class).text
                news.link = new_url
                self.data.append(news)
        return self.data
