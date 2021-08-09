from datetime import date, timedelta


class Product:
    def __init__(self, name, volume, expiration_date, freezable):
        self.freezable = freezable
        self.expiration_date = expiration_date
        self.volume = volume
        self.name = name

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_value):
        if not isinstance(new_value, (int, float)):
            raise TypeError(f"Incorrect volume type: {new_value}.")
        self._volume = new_value

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, new_expiration_date):
        if new_expiration_date <= date.today() + timedelta(days=1):
            raise ValueError(f'Product is outdated.')
        self._expiration_date = new_expiration_date

    def __str__(self):
        return self.name
