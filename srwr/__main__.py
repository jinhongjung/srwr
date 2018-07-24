import sys
from time import process_time as tic, process_time as toc
from srwr.reader import read_graph
from srwr.normalizer import semi_row_normalize

def main():
    path = 'data/slashdot.tsv'

    start = tic()
    A, base = read_graph(path)
    time = toc() - start
    print(f'read_time:\t{time:.4f} sec')

    start = tic()
    nAp, nAn = semi_row_normalize(A)
    time = toc() - start
    print(f'normalization_time:\t{time:.4f} sec')

if __name__ == "__main__":
    sys.exit(main())
