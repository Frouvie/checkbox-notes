import json

PATH = "data.json"
data = {
    "Anime": {
        "Berserk": "False",
        "Naruto": "False"
    }
}


def load_data():
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
