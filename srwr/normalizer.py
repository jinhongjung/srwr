import numpy as np
from scipy.sparse import csr_matrix, spdiags, find

def semi_row_normalize(A):
    m, n = A.shape

    # row-wise sum, d is out-degree for each node
    d = abs(A).sum(axis=1)

    d = np.maximum(d, np.ones((n, 1)))
    invd = 1.0/d
    invd = np.reshape(invd, (1, -1))
    invD = spdiags(invd, 0, m, n)
    snA = invD * A

    I, J, K = find(A)

    pos = K > 0;
    neg = K < 0;

    nAp = csr_matrix((abs(K[pos]), (I[pos], J[pos])), shape=(m, n))
    nAn = csr_matrix((abs(K[neg]), (I[neg], J[neg])), shape=(m, n))

    return nAp, nAn