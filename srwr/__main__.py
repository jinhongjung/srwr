import sys
from time import process_time as tic, process_time as toc
from srwr.srwr import SRWR
import numpy as np

def main():
    path = 'data/slashdot.tsv'

    # start = tic()
    # A, base = read_graph(path)
    # time = toc() - start
    # print(f'read_time:\t{time:.4f} sec')

    # start = tic()
    # nAp, nAn = semi_row_normalize(A)
    # time = toc() - start
    # print(f'normalization_time:\t{time:.4f} sec')

    srwr = SRWR()
    srwr.read_graph(path)
    srwr.normalize()

    seed = 49307

    rd, rp, rn, residuals = srwr.query(seed)
    print(rd)

    print(np.sum(rp) + np.sum(rn))

if __name__ == "__main__":
    sys.exit(main())
