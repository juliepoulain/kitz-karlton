from models.__init__ import CURSOR, CONN


class Reservation:

    all = {}

    def __init__(self, phone_number, length_of_stay, id=None):
        self.id = id
        self.phone_number = phone_number
        self.length_of_stay = length_of_stay

    def __repr__(self):
        return (
            f"<Reservation ID: {self.id}, "
            + f"Phone: {self.phone_number}, "
            + f"Length of Stay: {self.length_of_stay}>"
        )
    
    @property
    def phone_number


