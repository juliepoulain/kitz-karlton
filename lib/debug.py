#!/usr/bin/env python3
# lib/debug.py

from models.owner import Owner
import ipdb

def test():
    Owner.drop_table()
    Owner.create_table()
    test_owner = Owner.create("Julie", 9999999999, "901 e van buren")

test()

ipdb.set_trace()
