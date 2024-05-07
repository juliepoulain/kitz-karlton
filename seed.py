from lib.models.cat import Cat
from lib.models.owner import Owner
from lib.models.reservation import Reservation

Owner.drop_table()
Cat.drop_table()
Reservation.drop_table()
Owner.create_table()
Cat.create_table()
Reservation.create_table()
owner1 = Owner.create("Julie", 9785510848, "901 E van Buren Street")
cat1 = Cat.create("Olivia", "calico", 4, 2, owner1.id)
reservation1 = Reservation.create(9785510848, 3, 5)
owner2 = Owner.create("Hollis", 7202337895, "274a 5th Ave")
cat2 = Cat.create("Higgs", "tabby", 1, 2, owner2.id)
reservation2 = Reservation.create(7202337895, 6, 3)
