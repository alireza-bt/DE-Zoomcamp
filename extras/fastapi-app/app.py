from fastapi import FastAPI, HTTPException
import oracledb
import os
import logging
import getpass
from sqlalchemy import create_engine
import cx_Oracle

PORT = 8000

un = os.environ.get('PYTHON_USERNAME')
cs = os.environ.get('PYTHON_CONNECTSTRING')
pw = getpass.getpass(f'Enter password for {un}@{cs}: ')

app = FastAPI()

# Create a connection pool
pool = oracledb.create_pool(user=un, password=pw, dsn=cs, min=1, max=4, increment=1)

@app.get("/")
async def root():
    return {"message": "Hello World - from Ali"}

# export PYTHON_CONNECTSTRING AND PYTHON_USERNAME

# Endpoint to retrieve an order by ID
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    try:
        with pool.acquire() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT order_id, product_name, quantity FROM orders", (order_id,))
                result = cursor.fetchone()
                logging.info('done!')
                if result:
                    order = {
                        "order_id": result[0],
                        "product_name": result[1],
                        "quantity": result[2],
                    }
                    return order
                else:
                    raise HTTPException(status_code=404, detail="Order not found")
    except oracledb.Error as e:
        raise HTTPException(status_code=500, detail=f"Database error: {e}")
