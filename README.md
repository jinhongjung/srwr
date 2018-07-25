# srwr
Python Implementation for Signed Random Walk with Restart (SRWR)

This repository aims to implement Signed Random Walk with Restart (SRWR) model
which was proposed by the following paper:

* Personalized Ranking in Signed Networks using Signed Random Walk with
  Restart, Jinhong Jung, Woojung Jin, Lee Sael, and U Kang, 
  IEEE International Conference on Data Mining (ICDM) 2016, Barcelona, Spain. 

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
