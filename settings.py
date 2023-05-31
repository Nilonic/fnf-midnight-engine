"""no this doesn't modify itself, it modifies other files"""

if __name__ == "__main__":
    import sys
    sys.exit("this is not an executable, run \"main.py\"")

import json

def update_settings(key, value):
    # Load existing data from the JSON file
    try:
        with open('./assets/settings.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    # Update the data with the new key-value pair
    data[key] = value

    # Write the updated data back to the JSON file
    with open('./assets/settings.json', 'w') as file:
        json.dump(data, file)


def read_settings(key):
    # Load data from the JSON file
    try:
        with open('./assets/settings.json', 'r') as file:
            data = json.load(file)
            return data.get(key)
    except FileNotFoundError:
        return None

def check_and_init():
    try:
        with open('./assets/settings.json', 'r') as file:
            return
    except FileNotFoundError:
        data = {"up": "w","up_alt": "i","down": "s","down_alt": "k","left": "a","left_alt": "j","right": "d","right_alt": "l","fps": 60,"crashOnError": 0}
        with open('./assets/settings.json', 'w') as file:
            json.dump(data, file)