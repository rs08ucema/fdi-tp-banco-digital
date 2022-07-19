import json

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response
from models.client import Client, ClientAddress, client_id_generator
from db.client_loader import load_clients
from db.client_store import store_client_file

app = Flask(__name__)
clients: list = load_clients()
accounts: list = []


# Internal use
@app.route("/api/digital-bank/clients/", methods=['GET'])
def get_all_clients():
    return jsonify([cli.serialize() for cli in clients])


@app.route("/api/digital-bank/clients/<client_id>", methods=['GET'])
def get_client(client_id):
    for client in clients:
        if client.id == client_id:
            return jsonify(client.serialize())

    return jsonify({})


@app.route("/api/digital-bank/clients/", methods=['POST'])
def create_client():
    client = request.json

    try:
        new_client = Client(
            client_id_generator(),
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

        clients.append(new_client)

    except KeyError as key_err:
        missing_param = (key_err.__str__())
        return jsonify(
            error_code="ERROR_BAD",
            error_description="Bad request",
            error_body=missing_param
        ), 400

    return jsonify(new_client.serialize())


@app.route("/api/digital-bank/client-test", methods=['POST'])
def creat_test_data():
    client = request.json
    client['id'] = client_id_generator()
    client['role'] = request.args['role']
    store_client_file(client)

    print(request.args['role'])

    # response = make_response(client, 201)
    # return response

    return client, 200
