#!/usr/bin/env python3
# lib/debug.py

from models.owner import Owner
import ipdb

Owner.drop_table()
Owner.create_table()
test_owner1 = Owner.create("new", 9785510848, "new")
test_owner2 = Owner.create("julie", 9785510848, "test2")
test_owner1.delete()

ipdb.set_trace()
