import psycopg2
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from .database.database import config


class App:

    def __init__(self):
        pass

    async def setup(self):
        pass

    async def insert_row(self,num_pool, num_sauna):
        """ insert a new row into the visitors table """
        sql = """insert into visitors (num_pool_visitors, num_sauna_visitors,date ) values (%s,%s,%s)"""

        conn = None
        try:
            # read database configuration
            params = config()
            # connect to the PostgreSQL database
            conn = psycopg2.connect(**params)
            # create a new cursor
            cur = conn.cursor()
            # execute the INSERT statement
            cur.execute(sql, (num_pool, num_sauna, datetime.now()))
            # get the generated id back
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

    async def scrapper(self):
        url = "https://www.sumperksportuje.cz/aquacentrum/kryty-bazen"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        swm_count = soup.find(id="pool-part-count")
        sauna_count = soup.find(id="sauna-part-count")
        swm_count_str = str(swm_count.string).split("/")
        sauna_count_str = str(sauna_count.string).split("/")
        num_ppl_in_swim = int(swm_count_str[0])
        num_ppl_in_sauna = int(sauna_count_str[0])

        await self.insert_row(num_ppl_in_swim, num_ppl_in_sauna)
