from flask import Flask, render_template, request, redirect, url_for, flash
from utils import load_watchlist, save_watchlist, fetch_stock_data,get_news
import json


app = Flask(__name__)
app.secret_key = 'secret_key'

WATCHLIST = 'watchlist.txt'

@app.route('/', methods = ['GET','POST'])
def index():
    tickers = load_watchlist()
    print(type(tickers))
    if request.method == 'POST':
        ticker = request.form.get('ticker').upper().strip()
        if not ticker:
            flash('Please enter a valid ticker symbol','error')
        else:  
            print(ticker)
            data = fetch_stock_data(ticker)
            if data:
                if ticker not in tickers:
                    tickers.append(ticker)
                    save_watchlist(ticker)
                    flash(f'{ticker} added', 'success')
                else:
                    flash(f'{ticker} already in watchlist', 'info')


            else:
                flash(f'Could not fetch data for {ticker}', 'error')
            
            return redirect(url_for('index'))
        
    else:
        stocks_data = []
        print('here is the ticker in app.py before the loop')
        print(tickers)
        for ticker in tickers:
            data = fetch_stock_data(ticker.strip("'").strip('"'))
            if data:
                stocks_data.append(data)

            
        
        

        return render_template('index.html',stocks=stocks_data)






@app.route('/remove/<ticker>')
def remove(ticker):
    tickers = load_watchlist()

    # Check if the ticker exists in the list
    if ticker in tickers:
        # Remove the ticker
        tickers.remove(ticker)

        # Save the updated list back to the text file
        with open(WATCHLIST, 'w') as f:
            for t in tickers:
                f.write(f"{t}\n")  # Write each ticker as a new line

        flash(f'{ticker} removed', 'success')
    else:
        flash(f'{ticker} not in list', 'error')

    return redirect(url_for('index'))

@app.route('/get_news/<ticker>')
def load_news(ticker):
    news = get_news(ticker)

    # Fetch all stocks data as you did in the index route
    tickers = load_watchlist()
    stocks_data = []
    for ticker in tickers:
        data = fetch_stock_data(ticker.strip("'").strip('"'))
        if data:
            stocks_data.append(data)

    # Render the template with both stocks data and news
    return render_template('index.html', stocks=stocks_data, news=news)


if __name__ == '__main__':
    app.run(debug=True)