import sys
import time
import requests
import pygame

#Configuration
TICKERS = [('bitcoin', 'BTC'),
          ('ethereum', 'ETH'),
          ('solana', 'SOL'),
          ('hype', 'HYPE')]

VS_CURRENCY = 'usd'
FETCH_INTERVAL = 30
SCROLL_SPEED = 2

#pygame setup

pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Crypto Ticker")
font = pygame.font.SysFont(None, 64)
clock = pygame.time.Clock()

def fetchPrices():
    ids = ','.join([t[0] for t in TICKERS])
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids':ids,
        'vs_currencies':VS_CURRENCY,
        'include_24hr_change':'true'
    }

    resp = requests.get(url, params=params, timeout=5)
    return resp.json()

