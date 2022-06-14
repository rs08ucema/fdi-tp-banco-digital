
class Account:

    def __init__(self, id, account_number, title, category, cbu, amount, client_id, mile_points=None) -> None:
        self.id = id
        self.account_number = account_number
        self.title = title
        self.category = category
        self.cbu = cbu
        self.amount = amount
        self.transactions = []
        self.client_id = client_id
        self.mile_points = mile_points

    def _set_mile_points(self, points):
        self.mile_points = points

    def add_new_trx(self, new_trx):
        self.transactions.append(new_trx)

        if new_trx < 0:
            self._set_mile_points(abs(new_trx))


class GoldAccount(Account):

    def __init__(self, id, account_number, title, category, cbu, amount, client_id, mile_points=None) -> None:
        super().__init__(id, account_number, title, category, cbu, amount, client_id, mile_points)


class PremiumAccount(Account):

    def __init__(self, id, account_number, title, category, cbu, amount, client_id, mile_points=None) -> None:
        super().__init__(id, account_number, title, category, cbu, amount, client_id, mile_points)

    def _set_mile_points(self, points):
        self.mile_points = (points * 1.25)


class BlackAccount(Account):

    def __init__(self, id, account_number, title, category, cbu, amount, client_id, mile_points=None) -> None:
        super().__init__(id, account_number, title, category, cbu, amount, client_id, mile_points)

    def _set_mile_points(self, points):
        self.mile_points = (points * 1.50)


