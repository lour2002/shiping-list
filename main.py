import gkeepapi
import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

master_token = os.getenv('MASTER_TOKEN')

keep = gkeepapi.Keep()
keep.authenticate('borisdiaw12@gmail.com', master_token)

keep.sync()
shopinglist = keep.get('1NopFGnUhEvmKthvjAlqejRUL_xQXHEsNU0mSQEaLn5ijfukEQowKdzQ1wjTZ1Q')

list_items = []
for item in shopinglist.unchecked:
    # Using unchecked box as per the example.
    # To handle checked items, you could use:
    # checkbox = "☑" if item.checked else "☐"
    checkbox = "☐"
    list_items.append(f"{checkbox} {item.text}")

listText = "\n".join(list_items)

output_data = {
  "message": listText if listText else "No items in the shopping list.",
}

# To get a JSON formatted string
output_json_string = json.dumps(output_data, indent=2, ensure_ascii=False)

# Send data to webhook
url = 'https://hook.eu2.make.com/sqw6pylxxeszpdohu7fsv5cqu5jpmoln'
headers = {
    'x-make-apikey': os.getenv('X_MAKE_APIKEY'),
    'Content-Type': 'application/json'
}

try:
    response = requests.post(url, headers=headers, data=output_json_string.encode('utf-8'))
    response.raise_for_status()  # Raise an exception for bad status codes
    print(f"Webhook response: {response.status_code}")
    print(response.text)

    # Clear the shopping list by checking all items
    for item in shopinglist.unchecked:
        item.delete()
    keep.sync()
    print("Shopping list cleared.")
except requests.exceptions.RequestException as e:
    print(f"Error sending data to webhook: {e}")