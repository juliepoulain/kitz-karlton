#!/usr/bin/env python3
# lib/debug.py

from models.owner import Owner
from models.cat import Cat
import ipdb

Owner.drop_table()
Owner.create_table()
test_owner1 = Owner.create("new", 9785510848, "new")
test_owner2 = Owner.create("julie", 9785510848, "test2")
Cat.drop_table()
Cat.create_table()
test_cat1 = Cat.create("Olivia", "calico", 2, 2, test_owner2.id)
print(Owner.get_cats(test_owner2))

ipdb.set_trace()
