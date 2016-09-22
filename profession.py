# Zicheng Zhen and Richard Wang
# Software Development
# 2016-09-15
# HW#2 -- More Python

import csv, random

def parseCSV(filename):
    with open(filename, "r") as raw:
        reader = csv.reader(raw)
        parsed = dict(reader)
        del parsed["Job Class"]
        return parsed

def choose(data):
    seed = random.random() * 99.8; # seed value
    for key in data:
        # print ( seed ) 
        seed -= float(data[key])
        if seed < 0:
            return key
    return -1

foo = parseCSV("occupations.csv")
print(choose(foo));
