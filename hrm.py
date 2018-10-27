from readCSV import *
from write_info import write_info
from dic import get_dictionary
import os


def hrm():
    """
        :Synopsis: Transform data in all input files to output files with information we want
    """
    dir_path = 'test_data'
    out_path = 'results'
    if not os.path.isdir(out_path):
        os.mkdir(out_path)
    for f in os.listdir(dir_path):
        if f.endswith('.csv'):
            path = dir_path+"/"+f
            data = read_csv(path)
            v_data = validation(data)
            time, ecg = get_data(v_data)
            metrics = get_dictionary(time, ecg)
            write_info(out_path+"/"+f[:-4], metrics)


if __name__ == "__main__":
    hrm()
