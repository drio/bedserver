### Intro

This is a small python package that implements a REST service to read
[bedfile](http://genome.ucsc.edu/FAQ/FAQformat.html) data over http.

I am writing this to provide a backend for [DNAism](https://github.com/drio/dnaism).
With this server, only the necessary data points are sent back to the
client so visualization are extremely fast independently of the amount
of data we are exploring.

### Setup

`$ pip install bedserver`
