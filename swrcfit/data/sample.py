def sample():
    """get sample data as dictionary object"""
    import os
    here = os.path.abspath(os.path.dirname(__file__))
    # Filename of the sample data is hard-coded here
    sampledata = os.path.join(here, 'sample.txt')
    with open(sampledata) as f:
        s = f.read()
    data = ''
    obj = {}
    for line in s.splitlines():
        if len(line) > 1 and line[:2] == '--':
            d = dataset(data)
            if d['valid']:
                obj[d['Soil sample']] = d
            data = ''
        else:
            data += line+'\n'
    d = dataset(data)
    if d['valid']:
        obj[d['Soil sample']] = d
    return obj


def dataset(input):
    obj = {'valid': False, 'data': [], 'text': ''}
    array = []
    text = ''
    for line in input.splitlines():
        if len(line) > 1 and line[:2] == '--':
            break
        data = line.replace(',', ' ').split()
        text += line+'\n'
        obj['text'] = text
        if len(data) > 0 and data[0].replace(".", "").isdigit():
            obj['empty'] = False
            if len(data) < 2:
                obj['message'] = 'Error in input data: '+line
                return obj
            try:
                floatdata = [float(s) for s in data[:3]]
            except Exception:
                obj['message'] = 'Error in input data: '+line
                return obj
            if min(floatdata) < 0:
                obj['message'] = 'Negative value in input data: '+line
                return obj
            array.append(floatdata)
        elif '=' in data:
            d = line.split('=')
            if len(d) > 1:
                obj[d[0].strip()] = d[1].strip()
    if len(array) == 0:
        obj['empty'] = True
        return obj
    if len(array) < 3:
        obj['message'] = 'Error in input data: at least 3 dataset is required.'
        return obj
    import numpy as np
    array = np.array(array).T
    if min(array[0]) == max(array[0]):
        obj['message'] = 'All h values are same.'
        return obj
    obj['valid'] = True
    obj['data'] = array
    return obj
