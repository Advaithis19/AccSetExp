import sys, os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(current)

from memberset import MemberSet

import time

class HashSet(MemberSet):
    hs = None

    def setup(self):
        self.hs = set()

    def verify_membership(self, item):
        t1 = int(time.perf_counter_ns())
        is_mem = item in self.hs
        t2 = int(time.perf_counter_ns())

        return is_mem, (t2 - t1)/1000 

    def insert(self, item):
        t1 = int(time.perf_counter_ns())
        self.hs.add(item)
        t2 = int(time.perf_counter_ns())

        return (t2 - t1)/1000

    def remove(self, item):
        t1 = int(time.perf_counter_ns())
        self.hs.remove(item)
        t2 = int(time.perf_counter_ns())

        return (t2 - t1)/1000