from datetime import datetime

NOW = datetime.now()


class Promo:
    def __init__(self, name=None, expires=None):
        self.name = name
        self.expires = expires
        self.expired = True if ((self.expires - NOW).days < 0) else False


promo = Promo("test", datetime.now())
print(promo.name)
print(promo.expires)
print(promo.expired)
