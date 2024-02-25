from fastapi import FastAPI, HTTPException
import oracledb
import os
import logging
import configparser
config = configparser.ConfigParser()
config.read('config.ini')

oci_config = config['OCI']

app = FastAPI()

# create connection to oci using a wallet (mTLS)
connection=oracledb.connect(
    config_dir=oci_config['config_dir'],
    dsn=oci_config['dsn'],
    password=oci_config['password'],
    user=oci_config['user'],
    wallet_location=oci_config['wallet_location'],
    wallet_password=oci_config['wallet_password'],
)


@app.get("/")
async def root():
    return {"message": "Hello World - from Ali"}

# export PYTHON_CONNECTSTRING AND PYTHON_USERNAME

# Endpoint to retrieve an order by ID
@app.get("/orders/{order_id}")
def get_order(order_id: int):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT order_id, product_name, quantity FROM orders where order_id=:1", (order_id,))
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
