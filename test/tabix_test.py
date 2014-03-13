#!/usr/bin/env python

import sys
import pysam
import json
sys.path.append('..')


from bedserver import compute


if len(sys.argv) != 5:
    print "./tabix_test.py sample.bed.gz chrm start stop"
else:
    fn, chrm, start, stop = sys.argv[1:]
    dp = compute.data_points(fn, start, stop, chrm, 1, 44)
    print len(dp)
    print dp
    print json.dumps(dp)
