import sys, os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from ds.hashset import HashSet
from ds.accum.accumulator import Accumulator

import random, matplotlib.pyplot as plt, numpy as np

LOWER_LIMIT = 0
UPPER_LIMIT = pow(2, 22)

def main():

    time_series_acc = list()
    time_series_acc.append(0)

    time_series_hs = list()
    time_series_hs.append(0)

    time_series_acc_proofs = list()
    time_series_acc_proofs.append(0)

    hs_obj = HashSet()
    hs_obj.setup()

    acc = Accumulator()
    acc.setup()

    for i in range(LOWER_LIMIT, UPPER_LIMIT):
        rand_put_index = random.randrange(LOWER_LIMIT, UPPER_LIMIT)
        curr_put_reader = rand_put_index

        _ = hs_obj.insert(curr_put_reader)
        _ = acc.insert(curr_put_reader)

        if((i+1)%1000 == 0):
            total_time_taken_hs = 0
            total_time_taken_acc = 0
            total_time_taken_acc_proofs = 0
            
            for _ in range(0, 100):
                rand_get_index = random.randrange(LOWER_LIMIT, UPPER_LIMIT)
                curr_get_reader = rand_get_index
                
                _, time_taken_hs = hs_obj.verify_membership(curr_get_reader)
                total_time_taken_hs += time_taken_hs

                curr_reader_proof, time_taken_acc_proof = acc.prove_membership(curr_get_reader)
                _, time_taken_acc = acc.verify_membership(curr_get_reader, curr_reader_proof)
                total_time_taken_acc += time_taken_acc
                total_time_taken_acc_proofs += time_taken_acc_proof

            avg_time_taken_hs = total_time_taken_hs / 100
            time_series_hs.append(avg_time_taken_hs)

            avg_time_taken_acc = total_time_taken_acc / 100
            time_series_acc.append(avg_time_taken_acc)

            avg_time_taken_acc_proofs = total_time_taken_acc_proofs / 100
            time_series_acc_proofs.append(avg_time_taken_acc_proofs)

    visualize(time_series_hs, time_series_acc, time_series_acc_proofs)
        

def visualize(ts1, ts2, ts3):
    x_axis = np.array(i for i in range(LOWER_LIMIT, UPPER_LIMIT, 1000))
    y_axis1 = np.array(ts1)
    y_axis2 = np.array(ts2)
    y_axis3 = np.array(ts3)

    plt.plot(x_axis, y_axis1, label='Hashset verification')
    plt.plot(x_axis, y_axis2, label='Accumulator verification')
    plt.plot(x_axis, y_axis3, label='Accumulator proof generation')

    plt.xlabel('Number of items in set')
    plt.ylabel('Time in microseconds')

    plt.title('Hashset vs Accumulator')

    plt.show()


if __name__ == "__main__":
    main()
