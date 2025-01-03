from openai import OpenAI
import os
from dotenv import load_dotenv
from action import (
    get_response_time,
    get_current_time,
    get_weather,
    get_stock_price,
    get_random_joke,
    get_random_fact,
    get_currency_conversion,
    get_news_headlines,
    get_definition,
    roll_dice,
    flip_coin
)

from prompts import system_prompt
from json_helper import extract_json

# Load environment variables
load_dotenv()

# Create an instance of the OpenAI class
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text_with_conversation(messages, model = "gpt-3.5-turbo"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=messages
        )
    return response.choices[0].message.content

#Available actions

available_actions = {
    "get_response_time": get_response_time,
    "get_current_time": get_current_time,
    "get_weather": get_weather,
    "get_stock_price": get_stock_price,
    "get_random_joke": get_random_joke,
    "get_random_fact": get_random_fact,
    "get_currency_conversion": get_currency_conversion,
    "get_news_headlines": get_news_headlines,
    "get_definition": get_definition,
    "roll_dice": roll_dice,
    "flip_coin": flip_coin
}


user_prompt = """what is the current time?"""

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]
    


turn_count = 1
max_turns = 5


while turn_count < max_turns:
    print (f"Loop: {turn_count}")
    print("----------------------")
    turn_count += 1

    response = generate_text_with_conversation(messages, model="gpt-4")

    print(response)

    json_function = extract_json(response)

    if json_function:
            function_name = json_function[0]['function_name']
            function_parms = json_function[0]['function_parms']
            if function_name not in available_actions:
                raise Exception(f"Unknown action: {function_name}: {function_parms}")
            print(f" -- running {function_name} {function_parms}")
            action_function = available_actions[function_name]
            #call the function
            result = action_function(**function_parms)
            function_result_message = f"Action_Response: {result}"
            messages.append({"role": "user", "content": function_result_message})
            print(function_result_message)
    else:
         break