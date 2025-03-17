import pandas as pd
import os
import logging
from db_utils import get_connection, create_table

#  log setting
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extract(csv_file):
    logging.info(f"Extracting data from {csv_file}")
    return pd.read_csv(csv_file)

def transform(data):
    logging.info("Transforming data...")
    data['sale_date'] = pd.to_datetime(data['sale_date'])
    data['total_price'] = data['price'] * data['quantity']
    return data

def load(data):
    logging.info("Loading data into MySQL...")
    conn = get_connection()
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO sales (product_name, price, quantity, sale_date, total_price)
        VALUES (%s, %s, %s, %s, %s)
    ''', data[['product_name', 'price', 'quantity', 'sale_date', 'total_price']].values.tolist())

    conn.commit()
    cursor.close()
    conn.close()
    logging.info("Data successfully loaded!")

if __name__ == "__main__":
    logging.info("Starting ETL Pipeline")
    create_table()  
    data = transform(extract('data/sales_data.csv'))
    load(data)
    logging.info("ETL Pipeline Completed Successfully")
