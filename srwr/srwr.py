from srwr import reader, normalizer, iterator

class SRWR:
    normalized = False

    def __init__(self):
        pass


    def read_graph(self, input_path):

        self.A, self.base = reader.read_graph(input_path)
        self.d = abs(self.A).sum(axis=1)
        self.normalize()


    def normalize(self):
        if self.normalized == False:
            self.nAp, self.nAn = normalizer.semi_row_normalize(self.A)
            self.nApT = self.nAp.T
            self.nAnT = self.nAn.T
            self.normalized = True


    def query(self, seed, c=0.15, epsilon=1e-9, beta=0.5, gamma=0.5,
            max_iters=300, handles_deadend=True):

        seed = seed - self.base
        print("degree: %d" % self.d[seed])

        rd, rp, rn, residuals = iterator.iterate(self.nApT, self.nAnT, seed, c,
                epsilon, beta, gamma, max_iters, handles_deadend)

        return rd, rp, rn, residuals
