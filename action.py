import os
import requests
from datetime import datetime
import yfinance as yf
import random

# --------------------------
# Action: Get Response Time
# --------------------------
def get_response_time(url):
    """
    Returns the response time of a website (mock implementation).
    """
    mock_response_times = {
        "github.com": 0.5,
        "google.com": 0.3,
        "openai.com": 0.4
    }
    return mock_response_times.get(url, 0.2)  # Default response time

# --------------------------
# Action: Get Current Time
# --------------------------
def get_current_time():
    """
    Returns the current time in HH:MM:SS format.
    """
    now = datetime.now()
    return now.strftime("%H:%M:%S")

# --------------------------
# Action: Get Weather
# --------------------------
def get_weather(city):
    """
    Returns the current weather for a given city.
    """
    api_key = os.getenv("WEATHER_API_KEY")  # Add your API key to .env
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return f"Weather in {city}: {data['weather'][0]['description']}, Temperature: {data['main']['temp']}°C"
    else:
        return f"Failed to fetch weather for {city}."

# --------------------------
# Action: Get Stock Price
# --------------------------
def get_stock_price(ticker):
    """
    Returns the current stock price for a given ticker.
    """
    stock = yf.Ticker(ticker)
    price = stock.history(period="1d")['Close'].iloc[-1]
    return f"The current price of {ticker} is ${price:.2f}."

# --------------------------
# Action: Get Random Joke
# --------------------------
def get_random_joke():
    """
    Returns a random joke.
    """
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} {joke['punchline']}"
    else:
        return "Failed to fetch a joke."

# --------------------------
# Action: Get Random Fact
# --------------------------
def get_random_fact():
    """
    Returns a random fact.
    """
    facts = [
        "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not."
    ]
    return random.choice(facts)

# --------------------------
# Action: Get Currency Conversion
# --------------------------
def get_currency_conversion(amount, from_currency, to_currency):
    """
    Converts an amount from one currency to another.
    """
    api_key = os.getenv("CURRENCY_API_KEY")  # Add your API key to .env
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][to_currency]
        converted_amount = amount * rate
        return f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}"
    else:
        return f"Failed to convert currency."

# --------------------------
# Action: Get News Headlines
# --------------------------
def get_news_headlines(query):
    """
    Returns the latest news headlines for a given query.
    """
    api_key = os.getenv("NEWS_API_KEY")  # Add your API key to .env
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        headlines = [article["title"] for article in data["articles"][:5]]
        return "Latest headlines:\n" + "\n".join(headlines)
    else:
        return f"Failed to fetch news for {query}."

# --------------------------
# Action: Get Definition
# --------------------------
def get_definition(word):
    """
    Returns the definition of a word.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        definition = data[0]["meanings"][0]["definitions"][0]["definition"]
        return f"Definition of {word}: {definition}"
    else:
        return f"Failed to fetch definition for {word}."

# --------------------------
# Action: Roll a Dice
# --------------------------
def roll_dice():
    """
    Simulates rolling a dice and returns a random number between 1 and 6.
    """
    return f"You rolled a {random.randint(1, 6)}."

# --------------------------
# Action: Flip a Coin
# --------------------------
def flip_coin():
    """
    Simulates flipping a coin and returns "Heads" or "Tails".
    """
    return f"It's {random.choice(['Heads', 'Tails'])}."
