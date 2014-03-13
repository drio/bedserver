#!/usr/bin/env python

import pysam

tabixfile = pysam.Tabixfile("example.bed.gz")
for gtf in tabixfile.fetch('Chr1', 78000, 100000):
    #print gtf.contig, gtf.start, gtf.end, gtf.gene_id
    print gtf
