import sys
import numpy as np
from srwr.srwr import SRWR
import fire


def process_query(input_path, output_path, output_type, seed, c=0.15,
                  epsilon=1e-9, beta=0.5, gamma=0.5, max_iters=300,
                  handles_deadend=True):
    '''
    Processed a query to obtain a score vector w.r.t. the seeds

    inputs
        input_path : str
            path for the graph data
        output_path : str
            path for storing an RWR score vector
        output_type : str
            type of output {'rp', 'rn', 'rd', 'both'}
                * rp: a positive SRWR score vector
                * rn: a negative SRWR score vector
                * rd: a trusthworthiness vector, i.e., rd = rp - rn
                * both: both of rp and rn (1st column: rp, 2nd column: rn)
        seed : int
            seed for query
        c : float
            restart probability
        epsilon : float
            error tolerance for power iteration
        beta : float
            balance attenuation factor
        gamma : float
            balance attenuation factor
        max_iters : int
            maximum number of iterations for power iteration
        handles_deadend : bool
            if true, it will handle the deadend issue in power iteration
            otherwise, it won't, i.e., no guarantee for sum of RWR scores
            to be 1 in directed graphs
    '''

    srwr = SRWR()
    srwr.read_graph(input_path)
    srwr.normalize()
    rd, rp, rn, residuals = srwr.query(seed, c, epsilon, beta, gamma,
                                       max_iters, handles_deadend)

    write_vectors(rd, rp, rn, output_path, output_type)


def write_vectors(rd, rp, rn, output_path, output_type):
    '''
    Write vectors into a file
    '''
    if output_type is 'rp':
        X = rp
    elif output_type is 'rn':
        X = rn
    elif output_type is 'rd':
        X = rd
    elif output_type is 'both':
        X = np.column_stack((rp, rn))
    else:
        raise ValueError('Type of output should be {rp, rn, rd, both}')

    np.savetxt(output_path, X)


def main():
    fire.Fire(process_query)


if __name__ == "__main__":
    sys.exit(main())
