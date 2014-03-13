import pysam


def data_points(file_path, start, stop, chrm, step, size):
    start, stop, step, size = int(start), int(stop), int(step), int(size)
    points = []
    w_size = (stop-start)/size

    p_window = start + w_size
    w_vals = []
    tabixfile = pysam.Tabixfile(file_path)
    for gtf in tabixfile.fetch(chrm, start, stop):
        _chrm, _start, _end, _val = gtf.split()
        _start, _end, _val = int(_start), int(_end), int(_val)

        for coor in range(_start, _end):
            if coor < p_window:
                w_vals.append(_val)
            else:
                points.append(sum(w_vals)/len(w_vals))
                p_window = p_window + w_size
                w_vals = [_val]


    if len(w_vals) > 0:
        points.append(sum(w_vals)/len(w_vals))

    return points[0:size]
