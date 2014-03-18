import pysam


def data_points(file_path, start, stop, chrm, step, size):
    start, stop, step, size = int(start), int(stop), int(step), int(size)
    points = []
    w_size = (stop-start)/size
    print "compute(): w_size = %s" % w_size

    tabixfile = pysam.Tabixfile(file_path)
    i_start = start
    for i in range(size):
        w_vals = []
        for gtf in tabixfile.fetch(chrm, i_start, i_start+w_size):
            _chrm, _start, _end, _val = gtf.split()
            _start, _end, _val = int(_start), int(_end), int(_val)
            w_vals.append(_val)

        if len(w_vals) > 0:
            points.append(sum(w_vals)/len(w_vals))
        else:
            points.append(0)

        i_start = i_start + w_size

    print "compute(): len(points) = %s" % len(points)
    return points[0:size]
