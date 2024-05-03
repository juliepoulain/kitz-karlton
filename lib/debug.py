#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.cat import Cat

Cat.create_table()


ipdb.set_trace()
