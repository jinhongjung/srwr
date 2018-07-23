import numpy as np
from scipy.sparse import csr_matrix


def read_graph(path):
    '''
    Read the signed network from the path
    '''

    X = np.loadtxt(path, dtype=float, comments='#')
    m, n = X.shape

    if n <= 2 or n >= 4:
        raise FormatError('Invalid input format')

    base = np.amin(X[:, 0:2])

    if base < 0:
        raise ValueError('Out of range of node id: negative base')

    X[:, 0:2] = X[:, 0:2] - base
    rows = X[:, 0]
    cols = X[:, 1]
    data = X[:, 2]

    n = int(np.amax(X[:, 0:2]) + 1)

    A = csr_matrix((data, (rows, cols)), shape=(n, n))

    return A, base
