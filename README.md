# srwr
Python Implementation for Signed Random Walk with Restart (SRWR)

This repository aims to implement Signed Random Walk with Restart (SRWR) model
which was proposed by the following paper:

* [Personalized Ranking in Signed Networks using Signed Random Walk with
  Restart](https://datalab.snu.ac.kr/~jinhong/papers/srwrICDM2016.pdf), Jinhong Jung, Woojung Jin, Lee Sael, and U Kang, 
  IEEE International Conference on Data Mining (ICDM) 2016, Barcelona, Spain. 
  
The following materials (slides, matlab codes, and datasets) can be useful.
* You can download the slides for the paper [here](http://datalab.snu.ac.kr/~jinhong/slides/srwrICDM2016.pptx).
* The MATLAB version used in the paper can be downloaded [here](https://datalab.snu.ac.kr/srwr/resources/SRWR-v1.2.zip).
* The datasets used in the paper are available at [here](https://datalab.snu.ac.kr/srwr/).

## Installation
To install python packages used in this repository, type the followings:
```bash
cd srwr
pip install -r requirements.txt
```

## Usage
We provide the following simple command line usage:
```bash
python -m srwr --input-path data/sample.tsv --output-path output/scores.tsv --output-type rd --seed 3942
```

This command will compute the SRWR score vector w.r.t. the seed node given by `--seed` in the input graph specified by `--input-path`, and write the result vector into the target file in `--output-path`. 

## Input and Output Format
### Input Format
The default input of `srwr` represents the edge list of a graph with the following format (tab separated):
```
# format: source (int) \t target (int) \t sign (int)
1	2   +1
1	4   -1
2	3   +1
...
```
> Although we assume the sign is +1 or -1, any real number can be used as a signed weight of an edge in the input. 

### Output Format
The default output of `srwr` contains an SRWR score vector (`--output-type` is among `rp`, `rn`, and `rd`) w.r.t. the given seed node as follows:
```
# format : an SRWR score of i-th node
0.1232e-3
0.0349e-4
...
```

When `--output-type` is `both`, then the output consists of `rp` and `rn` as
follows:
```
# format : a positive SRWR score \t a negative SRWR score of i-th node
0.1232e-3   0.2322e-9
0.0349e-9   0.2939e-4
...
```

### How to Use `srwr` in My Codes?
The following example shows how to import `srwr` and compute an SRWR query.
```python
from srwr.srwr import SRWR
srwr = SRWR()
srwr.read_graph(input_path) # read graph from input_path
srwr.normalize() # do semi row-normalization
rd, rp, rn, residuals = srwr.query(seed, c, epsilon, beta, gamma, max_iters, handles_deadend) # compute an SRWR query w.r.t. seed
```

Note that `rp` is a positive SRWR score vector, `rn` is a negative SRWR score
vector, and `rd` is called a relative trusthworthiness score vector (i.e., rd =
rp - rn) indicating that the negative `rd` score of node `u` means `seed` considers node `u` as enemy while the positive one means `seed` considers node `u` as friend.


## Arguments of `srwr`
We summarize the input arguments of `srwr` in the following table:

| Arguments     | Explanation       | Default       | 
| --------------|-------------------|:-------------:|
| `input-path` |  Input path for a graph | `None`|
| `output-path` | Output path for storing a query result | `None`|
| `output-type` | Type of output vector {`rd`, `rp`, `rn`, `both`} | `None`|
| `seed` |  A single seed (query) node id | `None`|
| `c` | Restart probablity | `0.15`|
| `beta` | Balance attenuation factor | `0.5`|
| `gamma` | Balance attenuation factor | `0.5`|
| `epsilon` | Error tolerance for power iteration | `1e-9`|
| `max-iters` |  Maximum number of iterations for power iteration | `100`|
| `handles-deadend` |  If true, handles the deadend issue | `True`|
| `verbose` |  If true, it will show a progress bar over iterations | `True`|

Note the followings:
* For directed graphs, there might be deadend nodes whose outdegree is zero. In this case, a naive power iteration would incur leaking out scores. 
`handles_deadend` exists for such issue handling deadend nodes. With `handles_deadend`, you can guarantee that the sum of `rp + rn` vector is 1.
Otherwise, the sum would less than 1 in directed graphs. 
The strategy `srwr` exploits is that whenever a random surfer visits a deadend node, go back to a seed node (or one of seed nodes), and restart.

## How to test this repository?
We add a simple script to test codes in this repository. 
```bash
python3 -m unittest test.srwr_test
```

This command will test the codes on two testcases located in
`data/testcases-*`, and show the below messages if it passes the tests.
```bash
----------------------------------------------------------------------
Ran 2 tests in 0.186s

OK
```

## Citation
```
@inproceedings{conf/icdm/JungJSK16,
  author    = {Jinhong Jung and
               Woojeong Jin and
               Lee Sael and
               U. Kang},
  title     = {Personalized Ranking in Signed Networks Using Signed Random Walk with
               Restart},
  booktitle = {{IEEE} 16th International Conference on Data Mining, {ICDM} 2016,
               December 12-15, 2016, Barcelona, Spain},
  pages     = {973--978},
  year      = {2016},
}
```

## Todo
* [ ] Add a notebook for SRWR tutorial
* [ ] Add an option for global ranking of SRWR
* [ ] Add a link for describing the SRWR's global ranking
* [ ] Add a link for describing the deadend issue
