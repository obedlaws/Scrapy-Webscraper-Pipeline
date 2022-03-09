
from itemadapter import ItemAdapter
import psycopg2

class t100:

    def __init__(self):
        self.con = psycopg2.connect("dbname='books' user='<username>' host='<docker IP Address>' port='5432' password='<user password>'")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS top100books(
            book_name text PRIMARY KEY,
            publication_date date,
            author text,
            price money
            );""")

    def process_item(self, item, spider):
        self.cur.execute("INSERT INTO top100books VALUES (%s, %s, %s, %s)", [item['name'], item['publication_date'], item['author'], item['price']])
        self.con.commit()
        return item
