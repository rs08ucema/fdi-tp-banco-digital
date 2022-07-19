import json


def store_client_file(client):
    with open('src/db/test.json', 'w') as store_file:
        json.dump(client, store_file)
        print(f"client stored")
