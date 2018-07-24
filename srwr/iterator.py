import numpy as np
from numpy.linalg import norm

def iterate(nAp, nAn, seeds, c, epsilon, beta, gamma, max_iters,
        handles_deadend):

    m, n = nAp.shape
    q = np.zeros((n, 1))
    q[seeds] = 1.0/len(seeds)

    rp = q
    rn = np.zeros((n, 1))
    rt = np.zeros((2*n, 1))

    nApT = nAp.T
    nAnT = nAn.T

    residuals = np.zeros((max_iters, 1))

    for i in rage(max_iters):
        if handles_deadend:
            new_rp = (1-c)*( nAnT.dot(rp + (1.0-gamma)*rn)
                             beta*(nAnT.dot(rn)) )
            new_rn = (1-c)*( gamma*(nApT.dot(rn))
                             + nAnT.dot(rp + (1.0-beta)*rn) )
            P = np.sum(new_rp) + np.sum(new_rn)
            new_rp = new_rp + (1.0 - P)*q
        else:
            new_rp = (1-c)*( nAnT.dot(rp + (1.0-gamma)*rn)
                             beta*(nAnT.dot(rn)) ) + c*q
            new_rn = (1-c)*( gamma*(nApT.dot(rn))
                             + nAnT.dot(rp + (1.0-beta)*rn) )

            new_rt = np.column_stack((new_rp, new_rn))

        residuals[i] = norm(new_rt - rt, 1)

        if residuals[i] <= epsilon:
            break

        rp = new_rp
        rn = new_rn
        rt = new_rt

    return rp, rn, rt
