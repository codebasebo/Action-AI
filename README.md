# ActionAI

ActionAI is a Python-based AI system that runs in a loop of `Thought`, `Action`, `PAUSE`, and `Action_Response`. It uses OpenAI's GPT models to understand user queries and execute predefined actions to provide answers.

## Features
- Dynamic Action Execution
- Extensible Architecture
- OpenAI GPT Integration
- Predefined Action Library

## Available Actions

| Action | Description | Example |
|--------|-------------|---------|
| `get_response_time` | Check website response time | `get_response_time: learnwithhasan.com` |
| `get_current_time` | Get current time | `get_current_time` |
| `get_weather` | Get city weather | `get_weather: New York` |
| `get_stock_price` | Get stock price | `get_stock_price: AAPL` |
| `get_random_joke` | Get random joke | `get_random_joke` |
| `get_random_fact` | Get random fact | `get_random_fact` |
| `get_currency_conversion` | Convert currencies | `get_currency_conversion: 100 USD EUR` |
| `get_news_headlines` | Get news headlines | `get_news_headlines: technology` |
| `get_definition` | Get word definition | `get_definition: algorithm` |
| `roll_dice` | Roll a dice (1-6) | `roll_dice` |
| `flip_coin` | Flip a coin | `flip_coin` |

## Setup

1. Install dependencies:
```bash
pip install openai python-dotenv requests yfinance
```

2. Configure `.env` file:
```plaintext
OPENAI_API_KEY=your_openai_api_key_here
WEATHER_API_KEY=your_weather_api_key_here
CURRENCY_API_KEY=your_currency_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

3. Run the project:
```bash
python main.py
```

## Project Structure
```
ActionAI/
├── actions.py          # Action functions
├── main.py            # Main script
├── prompts.py         # System prompts
├── json_helper.py     # JSON utilities
├── .env               # Configuration
├── README.md          # Documentation
└── requirements.txt   # Dependencies
```

## Contributing
Open issues or submit pull requests on GitHub.



