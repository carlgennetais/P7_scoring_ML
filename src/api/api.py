from typing import Union

import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()

# load cleaned-transformed dataframe once
# use raw data instead for interpretability ?
customers = pd.read_pickle("../../data/processed/app_train_cleaned.pkl").set_index(
    "SK_ID_CURR"
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/ping")
def ping():
    return {"Ping successfull"}


@app.get("/customers")
def list_customers():
    # TODO performance
    return customers.head(1000).index.to_list()


@app.get("/customers/{customer_id}")
def read_single_customer(customer_id: int, q: Union[str, None] = None):
    if customer_id in customers.index:
        return customers.loc[customer_id, :].fillna("").to_dict()
    else:
        raise HTTPException(status_code=404, detail="Customer ID does not exist")


@app.get("/customers_stats")
def all_customers_stats():
    return customers.describe().loc[["count", "mean", "std"], :].to_dict()
