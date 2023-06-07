import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("scraper_data.db")
        self.cursor = self.conn.cursor()
    
    def create_table_news(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS news(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255),
                summary TEXT,
                publication_date TEXT,
                author VARCHAR(255),
                link TEXT,
                category VARCHAR(100)
            );
        """)
    
    def insert_data_news(self, data):
        for d in data:
            self.cursor.execute("""
                INSERT INTO news(title, summary, publication_date, author, link, category)
                VALUES(?, ?, ?, ?, ?, ?)
            """, (d.title, d.summary, d.publication_date, d.author, d.link, d.category))
        self.conn.commit()

    def get_news(self):
        cur = self.cursor.execute('SELECT title, summary FROM news')
        return cur.fetchall()

    def close_data_base(self):
        self.conn.close()
