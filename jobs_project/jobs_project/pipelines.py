# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
import pymongo


class PostgresPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            dbname="scrapy_db",
            user="scrapy_user",
            password="scrapy_password",
            host="postgres",
            port="5432",
        )
        self.cursor = self.connection.cursor()
        print("succesfully connected!")

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        try:
            query = """
                INSERT INTO raw_table (
                    slug, language, req_id, title, description, location_name,
                    street_address, city, state, country, country_code, postal_code,
                    update_date, create_date
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
            """

            values = (
                item["slug"],
                item["language"],
                item["req_id"],
                item["title"],
                item["description"],
                item["location_name"],
                item["street_address"],
                item["city"],
                item["state"],
                item["country"],
                item["country_code"],
                item["postal_code"],
                item["update_date"],
                item["create_date"],
            )

            self.cursor.execute(query, values)
            self.connection.commit()
        except psycopg2.IntegrityError as e:
            # Constraint violation or null constraint violation
            self.connection.rollback()
            print("Error inserting data into raw_table:", e)
        except psycopg2.InternalError as e:
            # Data type mismatch
            self.connection.rollback()
            print("Error inserting data into raw_table:", e)
        except psycopg2.Error as e:
            # Other database-related errors
            self.connection.rollback()
            print("Error inserting data into raw_table:", e)
