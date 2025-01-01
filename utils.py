import json
import yfinance as yf
import google.generativeai as genai
from dotenv import load_dotenv
import os
import requests

load_dotenv()

WATCHLIST = 'watchlist.txt'

def save_watchlist(tickers):
    with open(WATCHLIST, 'a') as f:
        # For each ticker, write it as a new line
        for ticker in tickers:
            f.write(f"{ticker}")
        f.write("\n")
    

def load_watchlist():
    
    stocks_list = []
    try:
        with open(WATCHLIST, 'r') as f:
            # Iterate over each line in the file
            for line in f:
                # Strip any trailing newline or spaces and append to the list
                stocks_list.append(line.strip())
        return stocks_list

    except FileNotFoundError:
        return []

def fetch_stock_data(ticker):
    try:
        print("here is the ticker in utils.py")
        print(ticker)
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')
        
        if not data.empty:
            row = data.iloc[-1]
            price = row['Close']
            high = row['High']
            low = row['Low']
            volume = row['Volume']
            prev_close = stock.info.get('previousClose',price)
            change = price - prev_close
            change_percent = (change / prev_close) * 100
            date_time = row.name.strftime('%Y-%m-%d %H:%M:%S')

            return_data = {
                'ticker':ticker,
                'price': f'${price:.2f}',
                'datetime': date_time,
                'change': round(change,2),
                'change_percent': round(change_percent,2),
                'high': f'${high:.2f}',
                'low': f'${low:.2f}',
                'volume': f'{volume:,}'
            }
            
            print(return_data)

            return return_data
        else:
            return None
        
    except Exception:
        return None
    

def get_news(ticker_symbol):
    # Your NewsAPI key
    api_key = os.getenv('NEWS_API_KEY')

    # Stock symbol (e.g., "AAPL" for Apple)
    stock_symbol = ticker_symbol

    # Define the endpoint URL with pageSize parameter to limit results to 5 articles
    url = f'https://newsapi.org/v2/everything?q={stock_symbol}&sortBy=publishedAt&pageSize=5&apiKey={api_key}'

    # Make the request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']
        
        # Print out the articles
        articles_data = []
        for article in articles:
            article_data ={
                'title': article['title'],
                'description': article['description'],
                'url': article['url']
            }
            articles_data.append(article_data)
        return articles_data
    else:
        print("Error fetching news")
        return None
