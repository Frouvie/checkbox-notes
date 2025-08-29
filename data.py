import os
import json

PATH = "data.json"
data = {}

def load_data():
    if not os.path.exists(PATH):
        save_data()
        return
    global data
    with open(PATH, "r") as file:
        data = json.load(file)


def save_data():
    with open(PATH, "w") as file:
        json.dump(data, file, indent=4)


def get_data():
    return data


def update_data(new_data):
    global data
    data = new_data
    save_data()


load_data()