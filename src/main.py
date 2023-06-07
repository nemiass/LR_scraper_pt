from scraper import LaRepublicaScraper
from data_base import Database
import sys
from tabulate import tabulate

def show_data(self):
    pass

def main():
    args = sys.argv

    if len(args) == 1:
        print("Exampe [main.py (start | show)]")
        return
    
    argument = args[1]

    try:
        if argument == "start":
            base_url ="https://larepublica.pe" 
            url = "https://larepublica.pe/ultimas-noticias"
            limit = 10
            lrscraper = LaRepublicaScraper(target_url=url, base_url=base_url, limit=limit)
            data = lrscraper.start_scraper()
            database = Database()
            database.create_table_news()
            database.insert_data_news(data)
            database.close_data_base()
            print("Scraping finish")

        elif argument == "show":
            database = Database()
            res = database.get_news()
            database.close_data_base()
            # display only title and summary
            headers = ['title', 'summary']
            print(tabulate(res, headers=headers, tablefmt='psql'))
    except Exception as e:
        print("ERROR: ", e)

if __name__ == "__main__":
    main()
