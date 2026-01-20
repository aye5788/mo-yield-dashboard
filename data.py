import requests
import streamlit as st

ALPHA_KEY = st.secrets["ALPHA_VANTAGE_KEY"]

def get_mo_price():
    url = (
        "https://www.alphavantage.co/query"
        f"?function=GLOBAL_QUOTE&symbol=MO&apikey={ALPHA_KEY}"
    )
    r = requests.get(url).json()
    return float(r["Global Quote"]["05. price"])


def get_mo_dividend():
    url = (
        "https://www.alphavantage.co/query"
        f"?function=DIVIDENDS&symbol=MO&apikey={ALPHA_KEY}"
    )
    r = requests.get(url).json()

    # Most recent quarterly dividend
    latest_dividend = float(r["data"][0]["amount"])

    # Annualize
    return latest_dividend * 4

