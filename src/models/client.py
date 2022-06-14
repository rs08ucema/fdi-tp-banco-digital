import random


def client_id_generator():
    return str(random.randint(1000000, 9000000))


class Client:

    def __init__(self, id, date_created, first_name, last_name, date_of_birth, document, gender, phone_number, email,
                 client_status, client_address) -> None:
        self.id = id
        self.date_created = date_created
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.document = document
        self.gender = gender
        self.phone_number = phone_number
        self.email = email
        self.client_status = client_status
        self.address: ClientAddress = client_address

    def serialize(self):
        return {
            'id': self.id,
            'date_create': self.date_created,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            # TODO add the rest of attributes

            'address': self.address.serialize()
        }


class ClientAddress:

    def __init__(self, street, street_number, city, state, post_code, country) -> None:
        self.street = street
        self.street_number = street_number
        self.city = city
        self.state = state
        self.post_code = post_code
        self.country = country

    def serialize(self):
        return {
            'street': self.state,
            'street_number': self.street_number,
            'city': self.city,
            'state': self.state,
            'post_code': self.post_code,
            'country': self.country
        }
