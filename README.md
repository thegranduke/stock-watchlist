# Stock Watchlist

This is a simple Flask web application designed to help you track a personalized watchlist of stocks. It provides real-time stock data, historical information, and relevant news articles, all in one convenient interface.

## Features

*   **Add Stocks:** Easily add stocks to your watchlist by entering their ticker symbols (e.g., AAPL, GOOG). The application handles case-insensitivity and whitespace trimming.
*   **Real-time Stock Data:** Displays key information for each stock, including:
    *   Current Price
    *   Date and Time of the last update
    *   Change from the previous closing price
    *   Percentage change
    *   Daily High
    *   Daily Low
    *   Volume
*   **Visual Cues:** Uses color-coding (green for positive change, red for negative change) to quickly visualize stock performance.
*   **Remove Stocks:** Remove stocks from your watchlist with a single click.
*   **News Integration:** Fetches and displays recent news articles related to each stock, providing context and insights. Links directly to the source articles.
*   **Error Handling:** Provides user-friendly flash messages for various scenarios, such as invalid ticker symbols, stocks already in the watchlist, and issues fetching data.
*   **Persistent Watchlist:** Your watchlist is saved to a text file (`watchlist.txt`), so it persists between sessions.

## Requirements

*   Python 3.7+ (Recommended)
*   Nodejs
*   Flask
*   yfinance
*   requests
*   python-dotenv (for managing environment variables)

You can install these dependencies using pip:

```
pip install -r requirements.txt`
```

## Installation and Setup

1. **Clone the Repository:**

Bash

`git clone https://github.com/thegranduke/stock-watchlist.git
cd stock-watchlist`

1. **Create a Virtual Environment (Recommended):**

```
python3 -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the environment (Linux/macOS)
venv\Scripts\activate  # Activate the environment (Windows)
```

1. **Install Dependencies:**
```
pip install -r requirements.txt
```

1. **Obtain a News API Key:** You'll need an API key from News API (https://newsapi.org/). Sign up for a free account to get one.
2. **Configure Environment Variables:** Create a `.env` file in the project's root directory and add your News API key:

`NEWS_API_KEY=YOUR_NEWS_API_KEY`

1. **Run the Application:**
```
python app.py
```

1. **Access the Application:** Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- **Adding Stocks:** Enter a stock ticker symbol in the input field and click "Add stock".
- **Viewing Data:** The table displays the current data for each stock in your watchlist.
- **Removing Stocks:** Click the "Remove" link next to a stock to remove it from the watchlist.
- **Viewing News:** Click the "Get News" link to see recent news articles related to the stock.
