import csv
from .simpledf import DataFrame

def is_float_able(val):
    try:
        val = float(val)
        return val
    except:
        return val

def read_csv(filename):
    data = DataFrame()
    with open(filename, "r") as f:
        features = [eval(x.strip().replace(".", "_")) for x in f.readline().split(",")]
        reader = csv.reader(f)
        for row in reader:
            for i, val in enumerate(row):
                setattr(data, features[i], is_float_able(val))    
    return data
