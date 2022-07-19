import json
from src.models.client import Client, ClientAddress


def load_clients():
    clients = []

    with open('src/db/clients_mock.json', 'r') as file:
        clients_json = json.load(file)
        for client in clients_json:
            clients.append(
                Client(
                    client['id'],
                    client['date_created'],
                    client['first_name'],
                    client['last_name'],
                    client['date_created'],
                    client['document'],
                    client['gender'],
                    client['phone_number'],
                    client['email'],
                    client['client_status'],
                    ClientAddress(
                        client['client_address']['street'],
                        client['client_address']['street_number'],
                        client['client_address']['city'],
                        client['client_address']['state'],
                        client['client_address']['post_code'],
                        client['client_address']['country']
                    )
                )
            )
    return clients
