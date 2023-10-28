
import pandas as pd
from sqlalchemy import create_engine
from time import time
import os
import argparse
#import polars as pl
import pyarrow.parquet as pq
import shutil

def main(params):
    user = params.user
    password = params.password
    host = params.host 
    port = params.port 
    db = params.db
    table_name = params.table_name
    url = params.url
    restart = params.restart
    
    # the backup files are gzipped, and it's important to keep the correct extension
    # for pandas to be able to open the file
    # if url.endswith('.csv.gz'):
    #     parquet_name = 'output.csv.gz'
    # else:
    #     parquet_name = 'output.csv'
    parquet_name = 'output.parquet'

    if restart.lower() == 'yes' or not os.path.isfile(parquet_name):
        print('re-downloading the file')
        os.system(f"wget {url} -O {parquet_name}")
        print('url %s'%url)
    else:
        print('Using the existing file')

    postgres_engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    try:
        #We want to avaoid out_of_memory and read the file in chunks
        #so we use pyarrow.parquet to read parquet in chunks.
        parquet_file = pq.ParquetFile(parquet_name)
        #sys.getsizeof(parquet_file)
        
        chunk_num = 0
        for i in parquet_file.iter_batches(batch_size=100000):
            df = i.to_pandas()

            # df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            # df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            if chunk_num == 0:
                df.head(n=0).to_sql(name=table_name, con=postgres_engine, if_exists='replace')
                print('Table created (or replaced)!')

            start = time()
            df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
            df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
            df.to_sql(name=table_name, con=postgres_engine, if_exists='append')
            end = time()

            print('Chunk %d done. it took: %.3f sec.' % (chunk_num, (end-start)))
            
            #test if it works
            #postgres_engine.connect()

            #get the DDL Query
            #print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=postgres_engine))

            #create table? do it for the first time and mind the first chunk that should be inserted in the db
            #df = next(df_iter)  
            #df.head(n=0).to_sql(name='yellow_taxi_data', con=postgres_engine, if_exists='replace')

            chunk_num += 1
    except Exception as e:
            print(e)
        
    #query data
    #df1 = pd.read_sql(sql='select * from yellow_taxi_data limit 10', con=postgres_engine)
    #df1.head()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True, help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True, help='database name for postgres')
    parser.add_argument('--table_name', required=True, help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')
    parser.add_argument('--restart', required=True, help='use the existing file or restart')

    args = parser.parse_args()

    main(args)