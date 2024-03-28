#!/usr/bin/env python

import requests


def get_info(crypto_id):
    return requests.get(f"https://api.coincap.io/v2/assets/{crypto_id}").json()


def waybar_output():
    return get_info("bitcoin")["data"]["priceUsd"]


btc_price = float(waybar_output())

print(f'{btc_price:.2f}')
