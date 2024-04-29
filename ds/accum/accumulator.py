import sys, os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(current)
sys.path.append(parent)

from memberset import MemberSet
from main import verify_membership, add, delete, setup, prove_membership

import time

class Accumulator(MemberSet):
    gen = None
    acc = None
    mod = None
    acc_set = None

    def setup(self):
        self.mod, self.acc, self.acc_set = setup()
        self.gen = self.acc

    def prove_membership(self, item):
        t1 = int(time.perf_counter_ns())
        proof = prove_membership(self.gen, self.acc_set, item, self.mod)
        t2 = int(time.perf_counter_ns())

        return proof, (t2 - t1)/1000 

    def verify_membership(self, item, proof):
        t1 = int(time.perf_counter_ns())
        is_mem = verify_membership(self.acc, item, self.acc_set, proof, self.mod)
        t2 = int(time.perf_counter_ns())

        return is_mem, (t2 - t1)/1000 

    def insert(self, item):
        t1 = int(time.perf_counter_ns())
        self.acc = add(self.acc, self.acc_set, item, self.mod)
        t2 = int(time.perf_counter_ns())

        return (t2 - t1)/1000

    def remove(self, item):
        t1 = int(time.perf_counter_ns())
        self.acc = delete(self.gen, self.acc, self.acc_set, item, self.mod)
        t2 = int(time.perf_counter_ns())

        return (t2 - t1)/1000