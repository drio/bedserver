### Intro

This is a small python package that implements a REST service to read
[bedfile](http://genome.ucsc.edu/FAQ/FAQformat.html) data over http.

I am writing this to provide a backend for [DNAism](https://github.com/drio/dnaism).
With this server, only the necessary data points are sent back to the
client so visualization are extremely fast independently of the amount
of data we are exploring.

### Setup

`$ pip install bedserver`

### Directory layout

The bedserver expects your data (bedfiles) to be divided in directories (projects) and 
bedfiles within them. The name of the bedfile (without) the extension is considered the 
sample name:

```
$ pwd
/Users/drio/dev/bedserver/test
$ find depth/
depth/
depth//18277.bed
depth//18277.bed.gz
depth//18277.bed.gz.tbi
depth//36013.bed
depth//36013.bed.gz
depth//36013.bed.gz.tbi
$ find snp_density/
snp_density/
snp_density//18277.YNPRC.Indian.chr1.bed
snp_density//18277.YNPRC.Indian.chr1.bed.gz
snp_density//18277.YNPRC.Indian.chr1.bed.gz.tbi
snp_density//19466.YNPRC.Indian.chr1.bed
snp_density//19466.YNPRC.Indian.chr1.bed.gz
snp_density//19466.YNPRC.Indian.chr1.bed.gz.tbi
```

Notice how all the bedfiles are indexed using [tabix](http://samtools.sourceforge.net/tabix.shtml). 

So here we have two projects: `depth` and `snp_density`. Within each projects we have two samples, for
the depth project we have: `18277` and `36013` and `18277.YNPRC.Indian.chr1` and `19466.YNPRC.Indian.chr1.bed` for
the snp_density project.


### Usage

Simply start the bedserver in the location where you have the bedfiles you want to 
serve:

```
$ cd /Users/drio/dev/bedserver/test
$ bedserver
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
 ...
```

Now let's use [curl](http://curl.haxx.se/) to interrogate the webserver, we have only two endpoins, 
one for listing the data (projects and samples) available and another one to query the data for an 
specific project and sample. Let's start with the first one:

```
curl -s 'http://localhost:5000/bedserver/api/v1.0/projects'
{
  "projects": {
    "depth": [
      "18277",
      "36013"
    ],
    "snp_density": [
      "18277.YNPRC.Indian.chr1",
      "19466.YNPRC.Indian.chr1"
    ]
  }
}
```

Let's now interrogate the server, asking for the data in a particular region given a project and sample. You 
probably want to take a look to [DNAism](https://github.com/drio/dnaism) to understand better the properties 
used here.

Let's query sample 18277, from project depth, genomic region Chr17:1100000-1102000. We want only 44 datapoints,
hence the size=44 property (look at  [DNAism](https://github.com/drio/dnaism) for more info).

```
curl -s 'http://localhost:5000/bedserver/api/v1.0/samples/depth/18277?start=1100000&stop=1102000&chrm=Chr17&step=1&size=44'
[39, 38, 30, 34, 44, 44, 41, 48, 45, 33, 36, 35, 34, 35, 35, 37, 33, 26, 28, 30, 35, 37, 32, 37, 49, 48, 41, 40, 44, 51, 46, 39, 40, 38, 45, 46, 38, 32, 37, 39, 36, 35, 44, 37]
```

Now, a similar query but for another project and sample:

```
curl -s 'http://localhost:5000/bedserver/api/v1.0/samples/snp_density/18277.YNPRC.Indian.chr1?start=2000000&stop=3000000&chrm=Chr1&step=1&size=44'
[9, 1, 1, 5, 20, 4, 1, 8, 26, 36, 50, 48, 46, 21, 37, 32, 28, 20, 26, 43, 35, 27, 61, 28, 36, 50, 55, 58, 42, 51, 37, 28, 49, 57, 52, 34, 22, 42, 48, 48, 44, 55, 43, 51]
```

